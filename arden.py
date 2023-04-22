import os
#from gtts import gTTS
import pyttsx3
from tempfile import TemporaryFile
import speech_recognition as sr
import webbrowser
import openai
import numpy as np
import requests
import configparser
import datetime
import spacy
from ctypes import *
import subprocess
import shlex

# Set the error handler function to suppress ALSA errors.
def alsa_error_handler(_, __, ___, ____, _____):
    pass

# Load the ALSA shared library.
alsa_lib = CDLL('libasound.so')

# Get the error handler function.
alsa_error_handler_func = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)(alsa_error_handler)

# Set the error handler function.
alsa_lib.snd_lib_error_set_handler(alsa_error_handler_func)

class VoiceAssistant:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.config = self.read_config()
        self.openweathermap_api_key = self.config.get("API_KEYS", "OpenWeatherMap")
        openai.api_key = self.config.get("API_KEYS", "OpenAI")
        self.wake_word = "Arden"  # Set your wake word here

    def read_config(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        return config

    def speak_text(self, text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[17].id)
        engine.say(text)
        engine.runAndWait()

    def save_speech_to_file(self, text, output_file):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[17].id)
        engine.save_to_file(text, output_file)
        engine.runAndWait()

    def get_intent(self, command):
        doc = self.nlp(command)
        intents = {
            "open_website": ["open", "website"],
            "ask_question": ["question", "ask"],
            "get_time_and_date": ["time", "date"],
            "set_alarm": ["alarm"],
            "get_weather": ["weather"]
        }

        for intent, keywords in intents.items():
            for keyword in keywords:
                if keyword in doc.text.lower():
                    return intent

        return None

# device_index=1

    def recognize_speech(self):
        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 2000  # Adjust the energy threshold
        recognizer.pause_threshold = 0.8  # Adjust the pause threshold
        recognizer.dynamic_energy_threshold = True  # Enable dynamic energy threshold
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.2)

            print("Listening...")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio)
                print(f"Heard: {command.lower()}")
                return command.lower()
            except:
                return None

    def listen_for_wake_word(self):
        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 2000  # Adjust the energy threshold
        recognizer.pause_threshold = 0.8  # Adjust the pause threshold
        recognizer.dynamic_energy_threshold = True  # Enable dynamic energy threshold
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            while True:
                print("Waiting for wake word...")
                audio = recognizer.listen(source)
                try:
                    speech = recognizer.recognize_google(audio)
                    print("Heard:", speech)
                    if self.wake_word.lower() in speech.lower():
                        return
                except:
                    pass

    def open_website(self, command):
        if 'google' in command:
            webbrowser.open('https://www.google.com')
        elif 'webservices' in command:
            webbrowser.open('https://kuma.billbert.co/status/webservices')

    def ask_chatgpt(self, command):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": command}
            ]
        )
        output = completion.choices[0].message.content
        output = output.strip().replace('\n', '')
        print(output)
        self.speak_text(f"Answer: {output}")

    def get_current_time_and_date(self):
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        date_str = now.strftime("%A, %B %d, %Y")
        return f"It's {time_str} on {date_str}."

    def extract_time_from_command(command):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(command)
        time_entities = [ent for ent in doc.ents if ent.label_ == "TIME"]
        
        if len(time_entities) > 0:
            return time_entities[0].text
        else:
            return None

    def set_alarm(self, time_str):
        # You can use a sound file or a script to be executed when the alarm goes off
        self.save_speech_to_file(f"BEEP, BEEP, BEEP, BEEP, BEEP, BEEP, BEEP, BEEP, BEEP, BEEP, BEEP", "reminder.wav")

        sound_file = "reminder.wav"
        command = f"aplay {sound_file}"
        
        # Create the 'at' command to schedule the alarm
        at_command = f"echo '{command}' | at {time_str}"
        
        # Execute the 'at' command using a subprocess
        process = subprocess.Popen(shlex.split(at_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            self.speak_text(f"Alarm has been set")
        else:
            self.speak_text(f"Failed to set alarm")

    def get_weather(self, city, api_key):
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
        response = requests.get(complete_url)
        
        if response.status_code == 200:
            data = response.json()
            main = data["main"]
            weather_data = data["weather"][0]
            temperature = main["temp"]
            humidity = main["humidity"]
            pressure = main["pressure"]
            weather_description = weather_data["description"]

            return {
                "temperature": temperature,
                "humidity": humidity,
                "pressure": pressure,
                "description": weather_description
            }
        else:
            return None


    def execute_task(self, command):
        intent = self.get_intent(command)
        if intent:
            print(f"Processing {intent}")
            self.speak_text(f"Processing command")

            if intent == "open_website":
                self.open_website(command)
            elif intent == "ask_question":
                self.ask_chatgpt(command)
            elif intent == "get_time_and_date":
                time_and_date = self.get_current_time_and_date()
                print(time_and_date)
                self.speak_text(time_and_date)
            elif intent == "get_weather":
                city = "Houston"  # Replace this with the desired city or parse the city name from the command
                weather_info = self.get_weather(city, self.openweathermap_api_key)
                if weather_info:
                    response = f"The weather in {city} is as follows: Temperature: {weather_info['temperature']}°C, Humidity: {weather_info['humidity']}%, Pressure: {weather_info['pressure']} hPa, Description: {weather_info['description']}."
                    print(response)
                    self.speak_text(response)  # Use your TTS function to speak the response
                else:
                    print("Failed to fetch weather data.")
                    self.speak_text("I'm sorry, I couldn't fetch the weather data.")
            elif intent == "set_alarm":
                # Parse the time from the command, e.g., "set alarm at 9:30 AM"
                time_str = self.extract_time_from_command
                self.set_alarm(time_str)

        else:
            self.speak_text(f"Apologies command not recognized")

# Usage example:
assistant = VoiceAssistant()

while True:
    assistant.listen_for_wake_word()
    print("Wake word detected!")
    assistant.speak_text("How can I help you?")
    command = assistant.recognize_speech()
    if command:
        assistant.execute_task(command)
    else: 
        assistant.speak_text("Sorry I did not hear your command")


# openai.api_key = api_key


# def read_config():
#     config = configparser.ConfigParser()
#     config.read("config.ini")
#     return config



# def speak_text(text):
#     engine = pyttsx3.init()
#     # Get the list of available voices
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[17].id)
#     engine.say(text)
#     engine.runAndWait()

# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#         try:
#             #command = transcribe_deepspeech(audio)
#             command = recognizer.recognize_google(audio)
#             return command.lower()
#         except:
#             return None

# def listen_for_wake_word(wake_word):
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         while True:
#             print("Waiting for wake word...")
#             audio = recognizer.listen(source)
            
#             try:
#                 # speech = transcribe_deepspeech(audio)
#                 speech = recognizer.recognize_google(audio)
#                 print("Heard:", speech)
#                 if wake_word.lower() in speech.lower():
#                     return
#             except:
#                 pass

# def open_website(command):
#     if 'google' in command:
#         webbrowser.open('https://www.google.com')
#     elif 'webservices' in command: 
#         webbrowser.open('https://kuma.billbert.co/status/webservices')
#     # Add more websites as needed

# def ask_chatgpt(command):
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "user", "content": command}
#         ]
#     )
#     output = completion.choices[0].message.content
#     output = output.strip().replace('\n', '')
#     print(output)
#     speak_text(f"Answer: {output}")

# def execute_task(command):
#     # if 'light' in command:
#     #     control_lights(command)
#     if 'open' in command:
#         open_website(command)
#     elif 'question' in command:
#         ask_chatgpt(command)
#     else: 
#         speak_text(f"Apologies command not recognized")

# if __name__ == "__main__":
#     wake_word = "Arden"

#     while True:
#         listen_for_wake_word(wake_word)
#         print("Wake word detected!")
#         speak_text("How can I help you?")

#         command = recognize_speech()
#         if command:
#             print("You said:", command)
#             speak_text(f"Executing: {command}")
#             execute_task(command)
#         else:
#             print("Couldn't recognize your command.")
#             speak_text("I'm sorry, I couldn't recognize your command.")
# model_path = './deepspeech/deepspeech-0.9.3-models.pbmm'
# scorer_path = './deepspeech/deepspeech-0.9.3-models.scorer'

# def transcribe_deepspeech(audio_data):
#     print("Entered DeepSpeech")
#     model = deepspeech.Model('deepspeech-0.9.3-models.pbmm')
#     model.enableExternalScorer('deepspeech-0.9.3-models.scorer')

#     # Adjust parameters
#     model.setBeamWidth(500)
#     model.setScorerAlphaBeta(alpha=0.75, beta=1.85)

#     # Convert SpeechRecognition's audio data to the format required by DeepSpeech
#     buffer = np.frombuffer(audio_data.frame_data, np.int16)

#     # Perform speech-to-text using DeepSpeech
#     text = model.stt(buffer)

#     print(f"Deepspeech transcribed: {text}")
#     return text

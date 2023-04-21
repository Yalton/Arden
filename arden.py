import os
#from gtts import gTTS
import pyttsx3
from tempfile import TemporaryFile
import speech_recognition as sr
import webbrowser
#import deepspeech
import openai
import numpy as np
import requests
import configparser
import datetime


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


# def speak_text(text):
#     tts = gTTS(text, lang='en')
#     with TemporaryFile() as temp_audio:
#         tts.save(temp_audio.name)
#         os.system(f"mpg123 {temp_audio.name}")

class VoiceAssistant:
    def __init__(self):
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

    def recognize_speech(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio)
                return command.lower()
            except:
                return None

    def listen_for_wake_word(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
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
        if 'open' in command:
            self.open_website(command)
        elif 'question' in command:
            self.ask_chatgpt(command)
        elif 'time' in command or 'date' in command:
            time_and_date = self.get_current_time_and_date()
            print(time_and_date)
            self.speak_text(time_and_date)
        elif "weather" in command:
            city = "Houston"  # Replace this with the desired city or parse the city name from the command
            weather_info = self.get_weather(city, self.openweathermap_api_key)
            if weather_info:
                response = f"The weather in {city} is as follows: Temperature: {weather_info['temperature']}°C, Humidity: {weather_info['humidity']}%, Pressure: {weather_info['pressure']} hPa, Description: {weather_info['description']}."
                print(response)
                self.speak_text(response)  # Use your TTS function to speak the response
            else:
                print("Failed to fetch weather data.")
                self.speak_text("I'm sorry, I couldn't fetch the weather data.")
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

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

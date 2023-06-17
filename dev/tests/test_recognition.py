import speech_recognition as sr

def record_and_transcribe():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Transcribing...")
        transcription = recognizer.recognize_google(audio)
        print("You said:", transcription)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")

if __name__ == "__main__":
    record_and_transcribe()

import pyttsx3

engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Print the details of each voice
for index, voice in enumerate(voices):
    print(f"Voice {index}:")
    print(f"  ID: {voice.id}")
    print(f"  Name: {voice.name}")
    print(f"  Languages: {voice.languages}")
    print(f"  Gender: {voice.gender}")
    print(f"  Age: {voice.age}")
    print()

# Set the desired voice by its index
desired_voice_index = 17  # You can change this index to try different voices

print(f"Sampling {voices[desired_voice_index].name}")

if desired_voice_index < len(voices):
    engine.setProperty('voice', voices[desired_voice_index].id)
else:
    print(f"No voice available at index {desired_voice_index}")

# Set the speech rate (words per minute)
engine.setProperty('rate', 150)

text = "Hello, this is a different voice."
engine.say(text)
engine.runAndWait()
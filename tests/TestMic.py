import pyaudio
import wave

# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "test_pyaudio.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open a new stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK,
                input_device_index=1)  # Set the device index to 1 (the index of your USB microphone)

print("Recording...")

frames = []

# Record audio
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording")

# Stop the stream and close it
stream.stop_stream()
stream.close()

# Terminate the PyAudio object
audio.terminate()

# Save the recorded data to a WAV file
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

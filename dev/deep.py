def transcribe_deepspeech(audio_data):
    print("Entered DeepSpeech")
    model = deepspeech.Model('deepspeech-0.9.3-models.pbmm')
    model.enableExternalScorer('deepspeech-0.9.3-models.scorer')

    buffer = audio_data.get_wav_data()
    print(f"Buffer length: {len(buffer)}")
    data16 = np.frombuffer(buffer, dtype=np.int16)
    print(f"data16 length: {len(data16)}")

    text = model.stt(data16)
    print(f"Deepspeech transcribed: {text}")
    return text
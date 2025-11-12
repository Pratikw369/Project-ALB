# file: coqui_mic_stt.py
import stt
import sounddevice as sd
import numpy as np

MODEL_PATH = "/home/prot/Projects/Project-ALB/testing_modules/STT/model/coqui/model.tflite"
SCORER_PATH = "/home/prot/Projects/Project-ALB/testing_modules/STT/model/coqui/huge-vocabulary.scorer"

model = stt.Model(MODEL_PATH)
model.enableExternalScorer(SCORER_PATH)

sr = 16000
def record_and_transcribe(duration=5):
    audio = sd.rec(int(duration*sr), samplerate=sr, channels=1, dtype="int16")
    sd.wait()
    text = model.stt(np.frombuffer(audio.tobytes(), np.int16))
    print("You said:", text)

print("🎙 Speak… Ctrl+C to stop")
while True:
    record_and_transcribe(5)

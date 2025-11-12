import sounddevice as sd
import numpy as np
import tempfile, soundfile as sf
from faster_whisper import WhisperModel

model = WhisperModel("small")
sr = 16000

print("🎙 Speak into the mic… Ctrl+C to stop")

def record_and_transcribe(duration=5):
    audio = sd.rec(int(duration*sr), samplerate=sr, channels=1, dtype="float32")
    sd.wait()
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        sf.write(f.name, audio, sr)
        wav = f.name
    segments, _ = model.transcribe(wav, beam_size=1)
    print("You said:", " ".join(s.text for s in segments))

while True:
    record_and_transcribe(5)

import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

# -------------------------------
# Queue for audio
# -------------------------------
q = queue.Queue()

def callback(indata, frames, time, status):
    """Called by sounddevice for each audio block"""
    if status:
        print(status, flush=True)
    q.put(bytes(indata))

# -------------------------------
# Load large Vosk model
# -------------------------------
ind_eng_small = "/home/prot/Projects/Project-ALB/testing_modules/STT/model/vosk-model-small-en-in-0.4"
ind_eng_large = "/home/prot/Projects/Project-ALB/testing_modules/STT/model/vosk-model-en-in-0.5"
us_eng_small = "/home/prot/Projects/Project-ALB/testing_modules/STT/model/vosk-model-small-en-us-0.15"

model = Model(ind_eng_large)
rec = KaldiRecognizer(model, 16000)
rec.SetWords(True)  # include word-level timing

# -------------------------------
# Start audio stream
# -------------------------------
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Listening with large Vosk model... Speak now. Press Ctrl+C to stop.")
    try:
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                text = res.get("text", "")
                if text.strip():
                    print("Final:", text)
            else:
                # partial result while speaking
                res = json.loads(rec.PartialResult())
                partial_text = res.get("partial", "")
                if partial_text.strip():
                    print("Partial:", partial_text, end='\r', flush=True)
    except KeyboardInterrupt:
        print("\nStopped listening.")

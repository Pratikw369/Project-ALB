import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

q = queue.Queue()
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

ind_eng_small = "/home/prot/Projects/Project-ALB/testing_modules/STT/model/vosk-model-small-en-in-0.4"
ind_eng_large = "/home/prot/Projects/Project-ALB/testing_modules/STT/model/vosk-model-en-in-0.5"
us_eng_small = "/home/prot/Projects/Project-ALB/testing_modules/STT/model/vosk-model-small-en-us-0.15"

model = Model(ind_eng_large)


rec = KaldiRecognizer(model, 16000)

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Listening...")
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            print("You said:", res.get("text", ""))

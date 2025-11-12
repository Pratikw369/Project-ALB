import threading
from TTS.api import TTS
import sounddevice as sd
import numpy as np

tts = TTS(model_name="tts_models/en/ljspeech/vits")

def generate_audio(text, buffer_list):
    audio = tts.tts(text=text)
    buffer_list.append(audio)

def play_audio(buffer_list):
    while not buffer_list:
        pass  # wait for audio
    audio = buffer_list.pop(0)
    sd.play(np.array(audio), samplerate=tts.synthesizer.output_sample_rate)
    sd.wait()

buffer_list = []
text = "Hello! I am your AI assistant. This is streaming TTS demo."
t1 = threading.Thread(target=generate_audio, args=(text, buffer_list))
t2 = threading.Thread(target=play_audio, args=(buffer_list,))
t1.start()
t2.start()
t1.join()
t2.join()

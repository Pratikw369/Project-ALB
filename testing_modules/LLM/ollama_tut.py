# from ollama import chat
# from ollama import ChatResponse
# import time
# start = time.time()

# response: ChatResponse = chat(model='llama3', messages=[
#   {
#     'role': 'user',
#     'content': 'hello',
#   },
# ])
# print(response['message']['content'])
# # or access fields directly from the response object
# print(response.message.content)

# end = time.time()

# print("time taken : ",end - start)

from TTS.api import TTS
import sounddevice as sd
import soundfile as sf

from ollama import chat
from ollama import ChatResponse
import time
#tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=True)

def play_wav(file_path: str):
    """Play a .wav file."""
    data, samplerate = sf.read(file_path)
    sd.play(data, samplerate)
   # sd.wait()  # Wait until playback is finished
    print(data,samplerate)

# in_chat = input("enter here")

# response: ChatResponse = chat(model='llama3', messages=[
#   {
#     'role': 'user',
#     'content': in_chat,
#   },
# ])

# tts.tts_to_file(text=response.message.content, file_path="ollama_tts.wav",speaker='p233' )

play_wav("/home/prot/Projects/Project-ALB/ollama_tts.wav")
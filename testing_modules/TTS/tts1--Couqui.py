from TTS.api import TTS
import sounddevice as sd
import soundfile as sf

speak = "You’re talking about taking an existing .wav file as input — so that means you don’t want to generate synthetic audio, but instead load and run a WAV file through your program (for playback, analysis, or maybe feeding it to a model)."

tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=True)
tts.tts_to_file(text=speak, file_path="output.wav", )


def play_wav(file_path: str):
    """Play a .wav file."""
    data, samplerate = sf.read(file_path)
    sd.play(data, samplerate)
    sd.wait()  # Wait until playback is finished



play_wav("output.wav")
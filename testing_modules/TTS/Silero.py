import torch
import soundfile as sf

print("Loading Silero TTS model...")
device = torch.device('cpu')  # or 'cuda' if you have GPU

# Load model (newer versions return tuple)
model, example_text = torch.hub.load(
    repo_or_dir='snakers4/silero-models',
    model='silero_tts',
    language='en',
    speaker='v3_en'
)

# Move model to device
model.to(device)

# Example text
text = """Good day, Professor. This is your personal AI assistant prototype,
designed to help with tasks, provide knowledge, and communicate smoothly
using natural speech. This demonstration showcases the integration of
artificial intelligence with voice technology for an interactive experience."""

# Speaker options (try: 'en_0', 'en_1', 'en_2', 'en_3')
speaker = 'en_0'

print(f"Generating speech with {speaker}...")
audio = model.apply_tts(
    text=text,
    speaker=speaker,
    sample_rate=48000
)

sf.write("silero_output.wav", audio, 48000)
print("Saved as silero_output.wav")

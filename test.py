# test.py
import os
from pydub import AudioSegment
from pydub.utils import which

# Add FFmpeg to PATH
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-2025-08-07-git-fa458c7243-full_build\bin"

# Set FFmpeg paths explicitly
FFMPEG_PATH = os.path.normpath(r"C:\ffmpeg-2025-08-07-git-fa458c7243-full_build\bin\ffmpeg.exe")
FFPROBE_PATH = os.path.normpath(r"C:\ffmpeg-2025-08-07-git-fa458c7243-full_build\bin\ffprobe.exe")

if not os.path.exists(FFMPEG_PATH):
    raise FileNotFoundError(f"FFmpeg not found at {FFMPEG_PATH}")
if not os.path.exists(FFPROBE_PATH):
    raise FileNotFoundError(f"FFprobe not found at {FFPROBE_PATH}")

AudioSegment.ffmpeg = FFMPEG_PATH
AudioSegment.ffprobe = FFPROBE_PATH
AudioSegment.converter = FFMPEG_PATH

print(f"FFmpeg path (via which): {which('ffmpeg')}")
print(f"FFprobe path (via which): {which('ffprobe')}")
print(f"FFmpeg path (set): {AudioSegment.ffmpeg}")
print(f"FFprobe path (set): {AudioSegment.ffprobe}")

mp3_path = os.path.normpath(r"C:\Users\Legion\OneDrive\Desktop\dora\output_test.mp3")
wav_path = os.path.normpath(r"C:\Users\Legion\OneDrive\Desktop\dora\output_test.wav")

if not os.path.exists(mp3_path):
    raise FileNotFoundError(f"MP3 file not found: {mp3_path}")

print(f"Loading MP3: {mp3_path}")
audio = AudioSegment.from_mp3(mp3_path)
print(f"Exporting to WAV: {wav_path}")
audio.export(wav_path, format="wav")
print(f"WAV file created: {wav_path}")
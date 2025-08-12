import os
import platform
import subprocess
from pydub import AudioSegment
from pydub.utils import which
from elevenlabs.client import ElevenLabs
import config

# Add FFmpeg to PATH
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-2025-08-07-git-fa458c7243-full_build\bin"

# Set FFmpeg paths explicitly for pydub
FFMPEG_PATH = os.path.normpath(r"C:\ffmpeg-2025-08-07-git-fa458c7243-full_build\bin\ffmpeg.exe")
FFPROBE_PATH = os.path.normpath(r"C:\ffmpeg-2025-08-07-git-fa458c7243-full_build\bin\ffprobe.exe")

if not os.path.exists(FFMPEG_PATH):
    raise FileNotFoundError(f"FFmpeg not found at {FFMPEG_PATH}")
if not os.path.exists(FFPROBE_PATH):
    raise FileNotFoundError(f"FFprobe not found at {FFPROBE_PATH}")

AudioSegment.ffmpeg = FFMPEG_PATH
AudioSegment.ffprobe = FFPROBE_PATH
AudioSegment.converter = FFMPEG_PATH

def play_mp3_directly(filepath):
    try:
        ffplay_path = os.path.normpath(r"C:\ffmpeg-2025-08-07-git-fa458c7243-full_build\bin\ffplay.exe")
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"MP3 file not found: {filepath}")
        if not os.path.exists(ffplay_path):
            raise FileNotFoundError(f"FFplay not found: {ffplay_path}")
        print(f"Playing MP3 with ffplay: {filepath}")
        subprocess.run([ffplay_path, "-nodisp", "-autoexit", filepath], check=True)
    except Exception as e:
        print(f"Playback error with ffplay: {e}")

def play_wav_via_powershell(filepath):
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"MP3 file not found: {filepath}")
        wav_path = filepath.replace('.mp3', '.wav')
        print(f"Loading MP3: {filepath}")
        audio = AudioSegment.from_mp3(filepath)
        print(f"Exporting to WAV: {wav_path}")
        audio.export(wav_path, format='wav')
        if not os.path.exists(wav_path):
            raise FileNotFoundError(f"WAV file not created: {wav_path}")
        print(f"Playing WAV via PowerShell: {wav_path}")
        subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_path}").PlaySync();'], check=True)
    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Playback error: {e}")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    try:
        client = ElevenLabs(api_key=config.elevenlabs_api_key)
        audio = client.text_to_speech.convert(
            text=input_text,
            voice_id="ZF6FPAbjXT4488VcRRnw",
            model_id="eleven_multilingual_v2",
            output_format="mp3_22050_32"
        )
        # Save audio by iterating over generator
        with open(output_filepath, "wb") as f:
            for chunk in audio:
                f.write(chunk)
        print(f"Saved audio to {output_filepath}")
        
        os_name = platform.system()
        try:
            if os_name == "Darwin":  # macOS
                subprocess.run(['afplay', output_filepath], check=True)
            elif os_name == "Windows":  # Windows
                play_wav_via_powershell(output_filepath)
                # Alternatively, uncomment to use ffplay
                # play_mp3_directly(output_filepath)
            elif os_name == "Linux":  # Linux
                subprocess.run(['aplay', output_filepath], check=True)
            else:
                raise OSError("Unsupported operating system")
        except Exception as e:
            print(f"An error occurred while trying to play the audio: {e}")
    except Exception as e:
        print(f"Error in text_to_speech_with_elevenlabs: {e}")

def text_to_speech_with_gtts(input_text, output_filepath):
    from gtts import gTTS
    language = "en"
    try:
        audioobj = gTTS(
            text=input_text,
            lang=language,
            slow=False
        )
        audioobj.save(output_filepath)
        print(f"Saved audio to {output_filepath}")
        
        os_name = platform.system()
        try:
            if os_name == "Darwin":  # macOS
                subprocess.run(['afplay', output_filepath], check=True)
            elif os_name == "Windows":  # Windows
                play_wav_via_powershell(output_filepath)
                # Alternatively, uncomment to use ffplay
                # play_mp3_directly(output_filepath)
            elif os_name == "Linux":  # Linux
                subprocess.run(['aplay', output_filepath], check=True)
            else:
                raise OSError("Unsupported operating system")
        except Exception as e:
            print(f"An error occurred while trying to play the audio: {e}")
    except Exception as e:
        print(f"Error in text_to_speech_with_gtts: {e}")

if __name__ == "__main__":
    # Debug FFmpeg detection
    print(f"FFmpeg path: {which('ffmpeg')}")
    print(f"FFprobe path: {which('ffprobe')}")

    input_text = "Hello guys.sudais kemon aso"
    output_filepath = os.path.normpath(r"C:\Users\Legion\OneDrive\Desktop\dora\output_test.mp3")

    print("Testing ElevenLabs TTS...")
    text_to_speech_with_elevenlabs(input_text, output_filepath)

    # print("Testing gTTS...")
    # text_to_speech_with_gtts(input_text, output_filepath)
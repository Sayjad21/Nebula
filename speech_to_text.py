import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import config
import time
import os

# Import Groq client for transcription
from groq import Groq
# Add FFmpeg to PATH
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-2025-08-07-git-fa458c7243-full_build\bin"
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Explicitly set FFmpeg paths for pydub
AudioSegment.ffmpeg = r"C:\ffmpeg-2025-08-07-git-fa458c7243-full_build\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg-2025-08-07-git-fa458c7243-full_build\bin\ffprobe.exe"
AudioSegment.converter = r"C:\ffmpeg-2025-08-07-git-fa458c7243-full_build\bin\ffmpeg.exe"

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Function to record audio from the microphone and save it as an MP3 file.

    Args:
        file_path (str): Path to save the recorded audio file.
        timeout (int): Maximum time to wait for a phrase to start (in seconds).
        phrase_time_limit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            # Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            # Verify the file was created and has content
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                logging.info(f"Audio saved to {file_path}, size: {file_size} bytes")
                if file_size == 0:
                    logging.error(f"File {file_path} is empty")
            else:
                logging.error(f"File {file_path} was not created")

    except Exception as e:
        logging.error(f"An error occurred during recording: {e}")

def transcribe_with_groq(audio_filepath):
    """
    Function to transcribe audio using Groq API.

    Args:
        audio_filepath (str): Path to the audio file.

    Returns:
        str: Transcribed text or None if an error occurs.
    """
    try:
        # Validate the audio file
        if not os.path.exists(audio_filepath):
            logging.error(f"File {audio_filepath} does not exist")
            return None
        if os.path.getsize(audio_filepath) == 0:
            logging.error(f"File {audio_filepath} is empty")
            return None

        client = Groq(api_key=config.groq_api_key)
        stt_model = "whisper-large-v3"
        with open(audio_filepath, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model=stt_model,
                file=audio_file,
                language="en"
            )
        return transcription.text

    except Exception as e:
        logging.error(f"An error occurred during transcription: {e}")
        return None

if __name__ == "__main__":
    filename = "test_audio.mp3"

    # Step 1: Record your voice
    record_audio(filename, timeout=10, phrase_time_limit=5)

    # Step 2: Wait a second for the file to be saved
    time.sleep(1)

    # Step 3: Transcribe using Groq
    result = transcribe_with_groq(filename)
    if result:
        print("\nTranscription:\n", result)
    else:
        print("\nTranscription failed.")
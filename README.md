# Dora AI Assistant

Dora is a multimodal AI assistant that supports:
- Text-to-speech (TTS) using ElevenLabs and Google gTTS
- Speech-to-text (STT) using Groq
- Image analysis using Groq Vision models
- Webcam capture
- Integration with LangChain and Gemini

## Features

- **Text-to-Speech:** Converts text to speech using ElevenLabs or Google gTTS.
- **Speech-to-Text:** Transcribes audio using Groq's API.
- **Image Analysis:** Captures webcam images and analyzes them with Groq Vision models.
- **Web UI:** Gradio-based interface for easy interaction.

## Setup

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/dora.git
cd dora
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

You also need [FFmpeg](https://ffmpeg.org/download.html) installed and available at:
```
C:\ffmpeg-2025-08-07-git-fa458c7243-full_build\bin
```
Or update the paths in the code to match your FFmpeg installation.

### 3. Configure API Keys

**DO NOT PUT SECRETS IN GIT!**

Create a file named `.env` (or `config.py` if you prefer, but make sure it's in `.gitignore`) with the following content:

```
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

Or, if using `config.py`:
```python
groq_api_key = "your_groq_api_key"
gemini_api_key = "your_gemini_api_key"
elevenlabs_api_key = "your_elevenlabs_api_key"
```

### 4. Run the application

```sh
python main.py
```

Or run individual modules for testing:

```sh
python text_to_speech.py
python speech_to_text.py
python tools.py
```

## Notes

- Make sure your webcam and microphone are connected and accessible.
- For Windows users, FFmpeg path must be set correctly in the code.
- All secret keys must be kept out of version control.

## File Structure

```
dora/
├── ai_agent.py
├── config.py         # (should NOT be committed)
├── main.py
├── requirements.txt
├── speech_to_text.py
├── test.py
├── text_to_speech.py
├── tools.py
├── .gitignore
└── README.md
```

## License

MIT License

---

**Never commit your API keys or secrets to

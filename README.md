Nebula is an AI-powered voice assistant that listens, thinks, and talks back—fast.
It combines Groq for lightning-speed speech recognition, ElevenLabs for lifelike voice synthesis, and Gradio for a sleek, interactive UI.

Whether you’re asking questions, telling jokes, or just chatting, Nebula makes every conversation fun, smooth, and futuristic.

✨ Features
🎙 Speech-to-Text — Powered by Groq’s whisper-large-v3 for accurate, real-time transcription.

🗣 Natural Voice Output — ElevenLabs turns text into silky-smooth speech.

📸 Live Webcam — Chat with a visual connection.

💬 Interactive UI — Built with Gradio for a responsive, user-friendly interface.

⚡ Low Latency — Near-instant speech recognition and playback.

🛠 Tech Stack
Technology	Purpose
Python	Core application logic
Groq Whisper	Speech-to-text processing
ElevenLabs TTS	Text-to-speech synthesis
Gradio	Web-based interface with webcam & chat
FFmpeg	Audio playback

📦 Installation
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/nebula.git
cd nebula
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Install FFmpeg

Windows — Download here & add to PATH

macOS —

bash
Copy
Edit
brew install ffmpeg
Linux —

bash
Copy
Edit
sudo apt install ffmpeg
Set up API keys
Create a config.py file in the project root:

python
Copy
Edit
groq_api_key = "YOUR_GROQ_API_KEY"
elevenlabs_api_key = "YOUR_ELEVENLABS_API_KEY"
▶️ Usage
Run Nebula:

bash
Copy
Edit
python nebula.py
From the Gradio interface:

🎥 Start webcam

🎙 Speak into your mic

💬 Chat with Nebula in real time

🛑 Say "goodbye" to end

📸 Interface Preview
Webcam View	Chat View
Live video feed	Real-time conversation

📜 License
MIT License — Free to use, modify, and distribute.

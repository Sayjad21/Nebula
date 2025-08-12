<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Nebula — Voice-powered AI Sidekick</title>
 
</head>
<body>
  <main class="container" role="main">
    <header>
      <div class="logo">NB</div>
      <div>
        <h1>Nebula — Voice-powered AI Sidekick</h1>
        <p class="lead">A witty, realtime voice assistant powered by Groq (STT), ElevenLabs (TTS), and Gradio (UI).</p>
      </div>
      <div class="badges">
        <div class="badge">Python</div>
        <div class="badge">Groq</div>
        <div class="badge">ElevenLabs</div>
        <div class="badge">Gradio</div>
      </div>
    </header>

    <section class="grid" aria-labelledby="about">
      <article class="card" id="about">
        <h2 style="margin-top:0;">What is Nebula?</h2>
        <p class="muted" style="color:var(--muted); margin:6px 0 12px;">
          Nebula listens to your voice, transcribes it with <strong>Groq</strong>, replies via an AI agent, and speaks back using <strong>ElevenLabs</strong>. The interface is built with <strong>Gradio</strong>, featuring a live webcam and chat pane for an immersive, realtime experience.
        </p>

        <h3>Main highlights</h3>
        <ul class="feature-list" aria-label="features">
          <li><strong>Speech-to-text:</strong> Groq — whisper-large-v3 (low latency)</li>
          <li><strong>Text-to-speech:</strong> ElevenLabs — natural, multi-lingual voices</li>
          <li><strong>UI:</strong> Gradio with webcam feed + chat window</li>
          <li><strong>Playback:</strong> MP3 via default system player or ffplay/ffmpeg fallback</li>
        </ul>
      </article>

      <aside class="card" aria-labelledby="tech">
        <h3 id="tech">Tech Stack</h3>
        <p class="muted">Clean, focused stack for fast prototyping and great UX.</p>
        <ul style="padding-left:14px; margin-top:8px; color:var(--muted);">
          <li><strong>Python</strong> — core logic</li>
          <li><strong>Groq API</strong> — speech-to-text (whisper-large-v3)</li>
          <li><strong>ElevenLabs</strong> — text-to-speech</li>
          <li><strong>Gradio</strong> — frontend UI with webcam</li>
          <li><strong>FFmpeg</strong> — audio conversion & playback</li>
        </ul>

        <h4 style="margin-top:12px;">Quick stats</h4>
        <p><span class="highlight">Realtime</span> • <span class="highlight">Low latency</span> • <span class="highlight">Multimodal</span></p>
      </aside>
    </section>

    <section class="card" aria-labelledby="install" style="margin-top:18px;">
      <h2 id="install">Installation</h2>
      <ol style="margin:10px 0 0 18px; color:var(--muted);">
        <li>Clone repo:
          <pre><code>git clone https://github.com/yourusername/nebula.git
cd nebula</code></pre>
        </li>
        <li>Install Python dependencies:
          <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Install FFmpeg:
          <pre><code>Windows: download from ffmpeg.org and add to PATH
macOS: brew install ffmpeg
Linux: sudo apt install ffmpeg</code></pre>
        </li>
        <li>Create <code>config.py</code> in the project root:
          <pre><code>groq_api_key = "YOUR_GROQ_API_KEY"
elevenlabs_api_key = "YOUR_ELEVENLABS_API_KEY"</code></pre>
        </li>
      </ol>
    </section>

    <section class="card" aria-labelledby="usage" style="margin-top:18px;">
      <h2 id="usage">Usage</h2>
      <p style="color:var(--muted); margin-top:6px;">Run Nebula locally and open the Gradio UI to start chatting by voice.</p>

      <pre><code>python nebula.py</code></pre>

      <h4 style="margin-top:8px;">UI actions</h4>
      <ul style="color:var(--muted);">
        <li><strong>Start camera</strong> — enable webcam feed</li>
        <li><strong>Speak</strong> — Nebula listens and transcribes</li>
        <li><strong>Chat</strong> — text chat shown on the right panel</li>
        <li><strong>Stop</strong> — say “goodbye” or close the UI</li>
      </ul>
    </section>

    <section class="card" aria-labelledby="examples" style="margin-top:18px;">
      <h2 id="examples">Examples</h2>
      <p style="color:var(--muted); margin-bottom:10px;">Example commands and behavior.</p>

      <pre><code>// casual
You: "Hey Nebula, tell me a joke."
Nebula: (speaks) "Why did the coder get kicked out of school? Because he kept breaking the class!"

// informational
You: "Nebula, summarize this article."
Nebula: (responds with a short summary, then reads it aloud)</code></pre>
    </section>

    <section class="card" aria-labelledby="tips" style="margin-top:18px;">
      <h2 id="tips">Tips & Troubleshooting</h2>
      <ul style="color:var(--muted);">
        <li><strong>FFmpeg warnings:</strong> If you see pydub warnings, set FFmpeg paths in code:
          <pre><code>from pydub import AudioSegment
AudioSegment.ffmpeg = r"C:\path\to\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\path\to\ffprobe.exe"</code></pre>
        </li>
        <li><strong>Playback on Windows:</strong> use <code>os.startfile(path)</code> to open MP3s with the default player.</li>
        <li><strong>API keys:</strong> keep <code>config.py</code> out of version control (add to <code>.gitignore</code>).</li>
      </ul>
    </section>

    <footer>
      <div>📄 <strong>License:</strong> MIT</div>
      <div class="right">⭐ Fork, tweak, and make Nebula your own</div>
    </footer>
  </main>
</body>
</html>


<h1 align="center">🎧 AI Audio Transcriber & Generator</h1>
<p align="center">A lightweight Flask web app to convert speech to text and text to speech in multiple languages.</p>


---



##   Features

- Upload .mp3, .wav, or other audio files for transcription.

- aste text or upload .txt files to convert text to speech.

- Download transcriptions and generated audio files.

- Supports multiple languages for text-to-speech.

- Clean web-based interface using Flask.

---

##  Live Preview
Coming soon — deploy with Render, Heroku, or Replit.

---

##  Tech Stack

Backend: Python + Flask

STT: SpeechRecognition

TTS: gTTS or pyttsx3

Audio Utils: pydub + FFmpeg

---


##  Folder Structure

```csharp

project-root/
├── app.py
├── requirements.txt
├── uploads/                # Uploaded & generated files
├── templates/              # HTML files
│   ├── home.html
│   ├── index.html
│   ├── tts.html
│   └── transcription.html (if exists)
├── static/                 # Optional for CSS/JS
└── README.md

```
##  Setup Instructions

1. Clone the repo

```bash

git clone https://github.com/yourusername/audio-transcriber.git
cd audio-transcriber
```

2. Install dependencies
```bash

pip install -r requirements.txt

```

3. Install FFmpeg
   
Required by pydub for audio processing:
Ubuntu/Debian

```bash

sudo apt update && sudo apt install ffmpeg
```

Windows/macOS
- Download from: https://ffmpeg.org/download.html

- Add ffmpeg to your system PATH


---

 ##  Run the App

```bash

python app.py
```
Then go to: http://127.0.0.1:5000

##  Routes & Pages

| Route         | Description                  |
| ------------- | ---------------------------- |
| `/`           | Home page                    |
| `/transcribe` | Upload audio for STT         |
| `/tts`        | Enter or upload text for TTS |

---



##   Customization Ideas

- Add TailwindCSS or Bootstrap for better UI

- Add Whisper or DeepSpeech for improved STT

- Add more TTS voice/language options

- Log user interactions or output history

  ---
  

##  Author : PriiiAiVerse

##   License
MIT License — feel free to use, modify, and share.


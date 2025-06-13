import os
from flask import Flask, request, render_template, redirect, url_for
import whisper
from flask import send_from_directory
import pyttsx3
from gtts import gTTS
# Set full path to ffmpeg manually
os.environ["PATH"] += os.pathsep + r"C:\Users\Dell\ffmpeg-7.0.2-essentials_build\bin"

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'm4a'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = whisper.load_model("base")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/")
def index():
    return redirect(url_for("upload_file"))

@app.route("/transcribe", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            #return f"File uploaded successfully: {file.filename}"
            # Transcribe with Whisper
            result = model.transcribe(audio=filepath)
            transcript = result["text"]

            # Save transcript to .txt file
            transcript_path = os.path.join(app.config["UPLOAD_FOLDER"], f"{os.path.splitext(file.filename)[0]}.txt")
            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(transcript)

            # Read from .txt and generate TTS
            with open(transcript_path, "r", encoding="utf-8") as f:
                text_to_speak = f.read()

            # Generate TTS audio
            tts_path = os.path.join(app.config["UPLOAD_FOLDER"], f"{os.path.splitext(file.filename)[0]}_tts.mp3")
            engine = pyttsx3.init()
            engine.save_to_file(transcript, tts_path)
            engine.runAndWait()

            return render_template("transcription.html", transcription=transcript, filename=file.filename,
                                   transcript_file=os.path.basename(transcript_path),
                                   tts_file=os.path.basename(tts_path))

            #return render_template("transcription.html", transcription=transcript, filename=file.filename)
            #return render_template("transcription.html", transcription=transcript, filename=file.filename,
                                   #transcript_file=os.path.basename(transcript_path))



            #return f"<h2>Transcription:</h2><p>{transcript}</p><a href='/transcribe'>Back</a>"
        else:
            return "File type not allowed"
            #return render_template("index.html")
    return render_template("index.html")





@app.route("/tts", methods=["GET", "POST"])
def text_to_speech():
    audio_file = None
    text = ""

    if request.method == "POST":
        text = request.form.get("text")
        lang = request.form.get("language", "en")
        textfile = request.files.get("textfile")

        if textfile and textfile.filename.endswith(".txt"):
            text = textfile.read().decode("utf-8")

        if not text:
            return "No text provided"

        tts = gTTS(text=text, lang=lang)
        audio_filename = "tts_output.mp3"
        audio_path = os.path.join(app.config["UPLOAD_FOLDER"], audio_filename)
        tts.save(audio_path)
        audio_file = audio_filename

    return render_template("tts.html", audio_file=audio_file, text=text)




@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)



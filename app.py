from flask import Flask, render_template, request
import whisper
import os
from transformers import pipeline

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load models once at startup
model = whisper.load_model("base")
sentiment_pipeline = pipeline("sentiment-analysis",
                              model="distilbert-base-uncased-finetuned-sst-2-english",
                              revision="714eb0f"
                              )

@app.route("/", methods=["GET", "POST"])
def index():
    transcription = ""
    sentiment = ""

    if request.method == "POST":

        if "audio" not in request.files:
            return "No file uploaded"

        file = request.files["audio"]

        if file.filename == "":
            return "No selected file"

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Transcribe audio
        result = model.transcribe(filepath)
        transcription = result["text"]

        # Sentiment analysis
        sentiment_result = sentiment_pipeline(transcription)

        sentiment = sentiment_result[0]["label"] + " (" + str(round(sentiment_result[0]["score"],2)) + ")"

    return render_template(
        "index.html",
        transcription=transcription,
        sentiment=sentiment
    )


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, render_template, jsonify
from config import Config
from ai_tool.gemini_ai import configure_api, generate_answer
from ai_tool.speech_utils import text_to_speech

app = Flask(__name__)
app.config.from_object(Config)

# Configure the API key
configure_api(app.config["GOOGLE_API_KEY"])

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.form.get("question", "")
        if not question:
            return render_template("index.html", error="Please enter a question.")
        try:
            # Generate answer using the AI model
            answer = generate_answer("gemini-pro", question)

            # Convert the answer to speech
            audio_file = text_to_speech(answer, output_file="static/audio.mp3")

            return render_template("index.html", question=question, answer=answer, audio_file=audio_file)
        except Exception as e:
            return render_template("index.html", error=str(e))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, send_file
import os
from utils import extract_and_summarize

app = Flask(__name__, static_folder='static', static_url_path='/static')
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None

    if request.method == "POST":
        # Text area input
        if request.form.get("text"):
            text_input = request.form["text"].strip()
            if text_input:
                file_path = os.path.join(UPLOAD_FOLDER, "temp_input.txt")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(text_input)
                summary = extract_and_summarize(file_path)

        # File upload input
        elif "file" in request.files:
            file = request.files["file"]
            if file and file.filename:
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)
                summary = extract_and_summarize(file_path)

    return render_template("index.html", summary=summary)

@app.route("/download", methods=["POST"])
def download():
    summary_text = request.form.get("summary_text", "")
    if summary_text:
        output_path = os.path.join(UPLOAD_FOLDER, "summary.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary_text)
        return send_file(output_path, as_attachment=True)
    return "No summary to download", 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

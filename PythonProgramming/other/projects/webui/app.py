from flask import Flask, render_template, request, session, redirect, url_for
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join("static", "upload")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

app = Flask(__name__, static_folder="assets", static_url_path="/assets")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/terms", methods=["GET"])
def terms():
    return render_template("pages/terms.html")

@app.route("/upload_page", methods=["GET"])
def upload_page():
    return render_template("pages/upload-page.html")

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload_files():
    uploaded_files = {}
    fields = ["model_img", "top1", "top2", "top3", "bottom1", "bottom2", "bottom3"]
    for field in fields:
        file = request.files.get(field)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(save_path)
            uploaded_files[field] = f"/static/upload/{filename}"
    occasion = request.form.get("occasion", "")
    return render_template("pages/upload-page.html", uploaded_files=uploaded_files, occasion=occasion)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
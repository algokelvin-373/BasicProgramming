from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__, static_folder="assets", static_url_path="/assets")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/terms", methods=["GET"])
def terms():
    return render_template("pages/terms.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
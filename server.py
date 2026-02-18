from flask import Flask, send_from_directory, jsonify, request
import subprocess
import os
import sys

# Folder where your files are
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=BASE_DIR, static_url_path='')

# Use the same Python that is running server.py (your venv one)
PYTHON = sys.executable


@app.route("/")
def index():
    # Serve index.html
    return send_from_directory(BASE_DIR, "index.html")


@app.post("/restart")
def restart():
    """
    Called by the Restart button.
    It should:
    1) Run RandomCircle.py  -> updates circle + mask + game_data.js
    2) Run DALLE.py         -> creates new Edited.png
    """
    try:
        # 1) Run RandomCircle.py
        print("▶ Running RandomCircle.py...")
        result1 = subprocess.run(
            [PYTHON, "RandomCircle.py"],
            cwd=BASE_DIR,
            capture_output=True,
            text=True
        )
        if result1.returncode != 0:
            print("❌ RandomCircle.py failed")
            print("STDOUT:", result1.stdout)
            print("STDERR:", result1.stderr)
            return jsonify({
                "status": "error",
                "step": "RandomCircle",
                "message": result1.stderr or "RandomCircle.py failed"
            }), 500

        # 2) Run DALLE.py
        print("▶ Running DALLE.py...")
        result2 = subprocess.run(
            [PYTHON, "DALLE.py"],
            cwd=BASE_DIR,
            capture_output=True,
            text=True
        )
        if result2.returncode != 0:
            print("❌ DALLE.py failed")
            print("STDOUT:", result2.stdout)
            print("STDERR:", result2.stderr)
            return jsonify({
                "status": "error",
                "step": "DALLE",
                "message": result2.stderr or "DALLE.py failed"
            }), 500

        print("✅ New puzzle generated successfully.")
        return jsonify({"status": "ok"})

    except Exception as e:
        # Catch anything unexpected
        print("❌ Unexpected error in /restart:", repr(e))
        return jsonify({
            "status": "error",
            "step": "server",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    # Run local dev server at http://127.0.0.1:5000/
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
from ai import generate_song, generate_instrument_part, assemble_song

app = Flask(__name__)
CORS(app)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"ok": True})

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json() or {}
    prompt = data.get("prompt", "").strip()
    if any(k in prompt.lower() for k in ["solo", "guitar", "trumpet", "piano", "sax", "violin", "drum"]):
        return jsonify(generate_instrument_part(prompt))
    return jsonify(generate_song(prompt))

@app.route("/api/assemble", methods=["POST"])
def assemble():
    data = request.get_json() or {}
    return jsonify(assemble_song(data))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

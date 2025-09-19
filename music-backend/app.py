from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/api/health")
def health():
    return jsonify(status="ok")

@app.post("/api/generate")
def generate():
    data = request.get_json(force=True)
    prompt = data.get("prompt", "")
    return jsonify({
        "type": "full_song",
        "key": "C minor",
        "tempo_bpm": 92,
        "chord_progression": ["Cm7", "Abmaj7", "Fm7", "G7"],
        "structure": [
            {"section": "Intro", "bars": 8},
            {"section": "Verse", "bars": 16},
            {"section": "Chorus", "bars": 16}
        ],
        "lyrics": "Hold the night while the city sleeps..."
    })

@app.post("/api/assemble")
def assemble():
    data = request.get_json(force=True)
    arrangement = data.get("arrangement", [])
    return jsonify({
        "stems": [
            {"name": "Drums", "url": "https://example.com/stems/drums.wav"},
            {"name": "Bass",  "url": "https://example.com/stems/bass.wav"},
            {"name": "Piano", "url": "https://example.com/stems/piano.wav"}
        ],
        "arrangement": arrangement
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

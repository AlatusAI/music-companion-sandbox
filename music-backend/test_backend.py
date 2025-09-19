import requests

BASE_URL = "https://special-chainsaw-jjwjgwjrrvqjcq6vg-5000.app.github.dev"

def test_health():
    try:
        res = requests.get(f"{BASE_URL}/api/health")
        print("✅ /api/health:", res.status_code, res.json())
    except Exception as e:
        print("❌ /api/health failed:", e)

def test_generate():
    try:
        payload = { "prompt": "Give me a lo-fi track with ambient textures" }
        res = requests.post(f"{BASE_URL}/api/generate", json=payload)
        print("✅ /api/generate:", res.status_code, res.json())
    except Exception as e:
        print("❌ /api/generate failed:", e)

def test_assemble():
    try:
        payload = { "arrangement": ["Intro", "Verse", "Chorus"] }
        res = requests.post(f"{BASE_URL}/api/assemble", json=payload)
        print("✅ /api/assemble:", res.status_code, res.json())
    except Exception as e:
        print("❌ /api/assemble failed:", e)

if __name__ == "__main__":
    test_health()
    test_generate()
    test_assemble()

def generate_song(prompt: str):
    return {
        "type": "full_song",
        "prompt": prompt,
        "key": "D minor",
        "tempo_bpm": 85,
        "chord_progression": ["Dm", "Bb", "F", "C"],
        "structure": [
            {"section": "intro", "bars": 4},
            {"section": "verse", "bars": 8},
            {"section": "chorus", "bars": 8},
            {"section": "verse", "bars": 8},
            {"section": "chorus", "bars": 8},
            {"section": "bridge", "bars": 8},
            {"section": "solo", "bars": 8},
            {"section": "chorus", "bars": 8},
            {"section": "outro", "bars": 4},
        ],
        "lyrics": """Verse 1:
Shadows of the city call my name...
Chorus:
I’m breaking out, I’m breaking free..."""
    }

def generate_instrument_part(prompt: str):
    return {
        "type": "instrument_part",
        "instrument": "guitar",
        "style_reference": "John Petrucci / Dream Theater",
        "key": "D minor",
        "tempo_bpm": 85,
        "techniques": ["legato", "wide vibrato", "melodic tapping", "string skipping"],
        "phrasing_notes": [
            "Open with a whole-step bend into D at the 15th fret.",
            "Use triplet arpeggio runs across Dm, Bb, F, C.",
            "Resolve phrases on chord tones; add delay and plate reverb."
        ],
        "tab_mock": "e|------------------| B|--15b17r15-13-----| G|--------------14--| ...",
        "midi_mock_url": None
    }

def assemble_song(context: dict):
    return {
        "project_id": context.get("project_id", "demo"),
        "arrangement": context.get("arrangement", ["intro","verse","chorus","verse","chorus","bridge","solo","chorus","outro"]),
        "stems": [
            {"name": "drums", "url": "/mock/stems/drums.wav"},
            {"name": "bass", "url": "/mock/stems/bass.wav"},
            {"name": "rhythm_guitar", "url": "/mock/stems/rhythm_guitar.wav"},
            {"name": "lead_guitar", "url": "/mock/stems/lead_guitar.wav"},
            {"name": "vocals", "url": "/mock/stems/vocals.wav"},
            {"name": "pads", "url": "/mock/stems/pads.wav"}
        ],
        "mix_notes": [
            "Solo after the second chorus.",
            "Boost vocals +1.5 dB at 2.5 kHz.",
            "Sidechain pads to kick."
        ]
    }

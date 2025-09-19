import React, { useState } from "react";
import axios from "axios";

const API = process.env.REACT_APP_API_BASE || "";

export default function ChatComposer() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const send = async (e) => {
    e.preventDefault();
    if (!prompt.trim()) return;
    setLoading(true);
    setResponse(null);
    try {
      const res = await axios.post(`${API}/api/generate`, { prompt });
      setResponse(res.data);
    } finally {
      setLoading(false);
    }
  };

  const assemble = async () => {
    setLoading(true);
    try {
      const res = await axios.post(`${API}/api/assemble`, {
        project_id: "demo",
        arrangement: response?.structure?.map(s => s.section)
      });
      setResponse(prev => ({ ...prev, assembled: res.data }));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <form onSubmit={send} style={{ display: "grid", gap: 10 }}>
        <textarea
          rows="4"
          placeholder="Describe the song you want (or ask for a Petrucci-style solo)..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />
        <button type="submit" disabled={loading}>{loading ? "Generating..." : "Generate"}</button>
      </form>

      {response && (
        <div style={{ marginTop: 20, textAlign: "left" }}>
          {response.type === "instrument_part" ? (
            <>
              <h3>Instrument Part</h3>
              <p><b>Instrument:</b> {response.instrument}</p>
              <p><b>Style:</b> {response.style_reference}</p>
              <p><b>Key:</b> {response.key} <b>Tempo:</b> {response.tempo_bpm} bpm</p>
              <ul>
                {response.phrasing_notes.map((n, i) => <li key={i}>{n}</li>)}
              </ul>
              <pre>{response.tab_mock}</pre>
            </>
          ) : (
            <>
              <h3>Full Song Draft</h3>
              <p><b>Key:</b> {response.key} <b>Tempo:</b> {response.tempo_bpm} bpm</p>
              <p><b>Chords:</b> {response.chord_progression?.join(" → ")}</p>
              <h4>Structure</h4>
              <ul>
                {response.structure?.map((s, i) => (
                  <li key={i}>{s.section} — {s.bars} bars</li>
                ))}
              </ul>
              <h4>Lyrics</h4>
              <pre>{response.lyrics}</pre>
              <button onClick={assemble} disabled={loading}>
                {loading ? "Assembling..." : "Assemble final version"}
              </button>
            </>
          )}

          {response.assembled && (
            <div style={{ marginTop: 20 }}>
              <h3>Final Assembly</h3>
              <ul>
                {response.assembled.stems.map((s, i) => (
                  <li key={i}>{s.name} — {s.url}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

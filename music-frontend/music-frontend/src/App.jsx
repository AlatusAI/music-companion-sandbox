import React from "react";
import ChatComposer from "./ChatComposer";

export default function App() {
  return (
    <div style={{ maxWidth: 900, margin: "0 auto", padding: 20 }}>
      <h1>MusicMindAI</h1>
      <p>Your AI music companion. Start with a feeling, end with a song.</p>
      <ChatComposer />
    </div>
  );
}

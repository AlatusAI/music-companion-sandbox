import React from "react";
import ChatComposer from "./ChatComposer";

export default function App() {
  return (
    <div style={{ maxWidth: 680, margin: "0 auto", padding: 20 }}>
      <h1>Music Companion</h1>
      <p>Try our Music companion. Start with a feeling, and watch a song pop up.</p>
      <ChatComposer />
    </div>
  );
}

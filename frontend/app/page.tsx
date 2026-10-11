"use client";

import { useState } from "react";

export default function Home() {
  const [story, setStory] = useState("");
  const [response, setResponse] = useState("");

  // API CALL FUNCTION
  const generateStory = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/story", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: story,
        }),
      });

      const data = await res.json();

      setResponse(JSON.stringify(data, null, 2));
    } catch (error) {
      setResponse("Error connecting to the backend.");
    }
  };

  return (
    <main>
      <h1>EMO-AI</h1>

      <h2>AI Emotional Storytelling Studio</h2>

      <textarea
        placeholder="Write or paste your story here..."
        rows={10}
        cols={50}
        value={story}
        onChange={(e) => setStory(e.target.value)}
      />

      <br />
      <br />

      <button onClick={generateStory}>
        Generate Story
      </button>

      <br />
      <br />

      <h3>Response:</h3>
      <pre>{response}</pre>
    </main>
  );
}
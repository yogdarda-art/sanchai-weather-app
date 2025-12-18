import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message) return;

    setLoading(true);
    setReply("");

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });

      const data = await res.json();
      setReply(data.reply);
    } catch {
      setReply("Error connecting to backend");
    }

    setLoading(false);
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        fontFamily: "Arial",
        backgroundColor: "#f5f5f5",
      }}
    >
      <div
        style={{
          background: "white",
          padding: "30px",
          borderRadius: "8px",
          boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
          textAlign: "center",
        }}
      >
        <h1>🌤️ AI Weather Assistant</h1>

        <input
          type="text"
          placeholder="Ask about weather"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          style={{ padding: "10px", width: "300px" }}
        />

        <br /><br />

        <button onClick={sendMessage} style={{ padding: "10px 20px" }}>
          Ask
        </button>

        <br /><br />

        {loading && <p>Thinking...</p>}
        {reply && <p><strong>Response:</strong> {reply}</p>}
      </div>
    </div>
  );
}

export default App;

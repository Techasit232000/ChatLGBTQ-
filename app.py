"""Flask web interface for ChatLGBTQ+."""

from flask import Flask, jsonify, render_template, request

from src.chatbot import Chatbot

app = Flask(__name__)
chatbot = Chatbot()


@app.get("/")
def index():
    """Render the chat interface."""
    return render_template("index.html")


@app.post("/api/chat")
def chat():
    """Return a chatbot response for a submitted message."""
    payload = request.get_json(silent=True) or {}
    message = str(payload.get("message", "")).strip()

    if not message:
        return jsonify({"error": "Message cannot be empty."}), 400

    response = chatbot.respond(message)
    return jsonify({"response": response})


@app.post("/api/reset")
def reset():
    """Clear the current conversation."""
    chatbot.reset_conversation()
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)

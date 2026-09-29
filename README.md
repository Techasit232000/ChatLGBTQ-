# ChatLGBTQ+

## Run the web interface

```bash
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

The current web interface uses the placeholder response in `src/chatbot.py`. Replace `Chatbot.respond()` with your selected AI provider integration before deploying, and keep API keys in `.env` rather than committing them.

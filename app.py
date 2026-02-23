from flask import Flask, jsonify, render_template_string
from config import Config
import random

app = Flask(__name__)

# Hardcoded fallback for Demo Mode to ensure 100% uptime
MOCK_AI_RESPONSES = [
    "This portfolio demonstrates full-stack skills.",
    "As an AI, I find the architecture robust.",
    "The animations utilize WebGL for high performance."
]

@app.route('/health')
def health():
    return jsonify({"status": "ok", "mode": "DEMO" if Config.DEMO_MODE else "LIVE"})

@app.route('/api/ai-query')
def ai_query():
    try:
        if Config.DEMO_MODE:
            return jsonify({"response": random.choice(MOCK_AI_RESPONSES), "source": "mock"})
        
        # Actual implementation would go here, wrapped in try/catch
        # raise Exception("Simulated outage")
        return jsonify({"response": "Live AI response", "source": "openai"})
    except Exception as e:
        app.logger.error(f"AI Error: {e}")
        return jsonify({"response": "Service temporarily unavailable.", "source": "fallback"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

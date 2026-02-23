from flask import Flask, request, jsonify
from pydantic import ValidationError
from app.config import settings
from app.security import authenticate
from app.validators import AIRequest
from app.ai_service import get_completion

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route('/api/v1/generate', methods=['POST'])
def generate():
    auth_error = authenticate()
    if auth_error:
        return auth_error

    try:
        body = request.get_json()
        req = AIRequest(**body)
        result = get_completion(req.prompt, req.temperature)
        return jsonify({"result": result}), 200
    except ValidationError as e:
        return jsonify({"error": "Validation Failed", "details": e.errors()}), 400
    except RuntimeError as e:
        app.logger.error(f"Service failure: {e}")
        return jsonify({"error": "Service unavailable"}), 503
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

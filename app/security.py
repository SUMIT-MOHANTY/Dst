from flask import request, jsonify
from app.config import settings

def authenticate():
    client_key = request.headers.get("X-API-KEY")
    if not client_key or client_key != settings.APP_API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    return None

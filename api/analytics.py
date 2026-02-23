from flask import Blueprint, request, jsonify
from functools import wraps
import hashlib
import uuid

analytics_bp = Blueprint('analytics', __name__)

def validate_payload(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.content_type != 'application/json':
            return jsonify({"error": "Invalid content type"}), 400
        return f(*args, **kwargs)
    return decorated

@analytics_bp.route('/event', methods=['POST'])
@validate_payload
def track_event():
    data = request.get_json()
    
    # Sanitize and hash potential PII
    user_agent = data.get('userAgent', 'unknown')[:200]
    user_hash = hashlib.sha256(user_agent.encode()).hexdigest()[:16]
    
    # Safe data model - no PII stored
    event = {
        'event_id': str(uuid.uuid4()),
        'category': data.get('category', '')[:50],
        'action': data.get('action', '')[:50],
        'label': data.get('label', '')[:100],
        'path': data.get('path', '/')[:200],
        'user_hash': user_hash,
        'timestamp': int(data.get('timestamp', 0) / 1000)
    }
    
    # In production: Store to secure database with encryption
    print(f"[ANALYTICS] Event logged: {event['category']} - {event['action']}")
    
    return jsonify({"status": "recorded"}), 202

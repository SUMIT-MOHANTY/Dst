from flask import Blueprint, request, jsonify
from ..models.contact import Contact, db
from ..schemas.contact_schema import ContactSchema
from ..utils.sanitizer import sanitize_string

contact_bp = Blueprint('contact', __name__)
schema = ContactSchema()

@contact_bp.route('/api/contact', methods=['POST'])
def handle_contact():
    try:
        # 1. Parse JSON
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        # 2. Validation (Schema + Length)
        errors = schema.validate(data)
        if errors:
            return jsonify({"error": "Validation failed", "details": errors}), 400

        # 3. Sanitization (XSS Prevention)
        clean_name = sanitize_string(data.get('name'))
        clean_email = sanitize_string(data.get('email'))
        clean_message = sanitize_string(data.get('message'))

        # 4. Storage (SQL Injection Prevention via ORM)
        new_contact = Contact(name=clean_name, email=clean_email, message=clean_message)
        db.session.add(new_contact)
        db.session.commit()

        return jsonify({"message": "Contact received", "id": new_contact.id}), 201

    except Exception as e:
        # Logging should happen here, e.g., app.logger.error(str(e))
        # Do not return full stack trace to user
        db.session.rollback()
        return jsonify({"error": "Internal Server Error"}), 500

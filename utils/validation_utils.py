import re
from html import escape

def validate_contact_payload(data: dict) -> tuple[bool, dict, list]:
errors = []
cleaned = {}

if not data:
return False, {}, ['No data provided']

name = data.get('name', '').strip()
email = data.get('email', '').strip()
message = data.get('message', '').strip()

if len(name) < 2:
errors.append('Name is too short.')

email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if not re.match(email_regex, email):
errors.append('Invalid email format.')

if len(message) < 10 or len(message) > 1000:
errors.append('Message must be between 10 and 1000 characters.')

# Sanitize output to be safe for logging or DB entry
cleaned = {
'name': escape(name),
'email': escape(email),
'message': escape(message)
}

is_valid = len(errors) == 0
return is_valid, cleaned, errors

# Flask Production Setup

Environment Variables:
- FLASK_ENV=production
- FLASK_DEBUG=0
- SECRET_KEY (set to strong random string)

Session Security:
- SESSION_COOKIE_SECURE=True
- SESSION_COOKIE_HTTPONLY=True
- SESSION_COOKIE_SAMESITE=Lax

Run with: python app_prod.py

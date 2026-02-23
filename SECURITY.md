# Security Guidelines

## Session Management
- Flask-Login handles secure session management
- Sessions are regenerated on login to prevent session fixation
- 'strong' session protection detects suspicious session changes

## Cookie Security
- In production, set `SECURE_COOKIES=True` to enable HTTPS-only cookies
- HTTPOnly flag prevents JavaScript access to cookies
- SameSite='Lax' prevents CSRF attacks

## Password Storage
- Passwords are hashed using Werkzeug's PBKDF2
- Default credentials: admin / SecureAdminPassword123!
- CHANGE THE DEFAULT PASSWORD IMMEDIATELY

## Deployment Checklist
1. Generate a strong SECRET_KEY using: `python -c 'import secrets; print(secrets.token_hex(32))'`
2. Set SECURE_COOKIES=True in production
3. Use HTTPS in production
4. Replace in-memory user database with a real database
5. Implement rate limiting on login endpoint
6. Add CSRF protection to all forms

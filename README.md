# AI Backend Service

A Flask-based backend service for handling AI requests with OpenAI integration.

## Setup

1. Copy .env.example to .env
2. Add your OpenAI API key
3. Install dependencies: pip install -r requirements.txt
4. Run: python main.py

## Endpoints

- GET /api/ai/health - Health check
- POST /api/ai/generate - Generate AI response
- POST /api/ai/validate - Validate API configuration

## Testing

Run tests: python -m pytest tests/

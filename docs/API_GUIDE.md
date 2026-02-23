# API Usage Guide

## Authentication
Include \`Authorization: Bearer <token>\` header.

## Endpoints

### GET /api/v1/status
Returns service health.

### POST /api/v1/auth/login
Body: \`{"username":"string","password":"string"}\`

## Error Codes
- 400: Bad Request
- 401: Unauthorized
- 500: Internal Server Error

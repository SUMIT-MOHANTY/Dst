<<<<<<< HEAD
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
=======
from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel, Field
import os
from openai import OpenAI
import uvicorn

app = FastAPI(title="AI API Service")

class AIRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=4000)
    model: str = Field(default="gpt-4")

class AIResponse(BaseModel):
    response: str
    model: str

def get_api_key(x_api_key: str = Header(..., alias="X-API-Key")):
    if not x_api_key or x_api_key != os.getenv("SERVICE_API_KEY", "dev-key"):
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/api/generate", response_model=AIResponse)
def generate(request: AIRequest, api_key: str = Depends(get_api_key)):
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")
    client = OpenAI(api_key=openai_key)
    try:
        response = client.chat.completions.create(
            model=request.model,
            messages=[{"role": "user", "content": request.prompt}]
        )
        ai_text = response.choices[0].message.content
        return AIResponse(response=ai_text, model=request.model)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
>>>>>>> aceb7be (Agent: AI Feature Backend Service)

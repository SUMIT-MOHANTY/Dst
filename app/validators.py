from pydantic import BaseModel, Field, field_validator
from app.config import settings

class AIRequest(BaseModel):
    prompt: str = Field(..., max_length=settings.MAX_PROMPT_LENGTH)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)

    @field_validator('prompt')
    @classmethod
    def check_prompt_safety(cls, v):
        if "<script>" in v.lower():
            raise ValueError("Potentially malicious content detected")
        return v.strip()

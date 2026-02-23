from pydantic import BaseModel, Field, validator
from typing import List, Optional

class Message(BaseModel):
    role: str = Field(..., description="Must be 'user' or 'assistant'")
    content: str = Field(..., min_length=1, max_length=1000)

class ChatRequest(BaseModel):
    session_id: str
    conversation_history: List[Message]
    user_query: str
    
    @validator('user_query')
    def sanitize_query(cls, v):
        v = v.strip()
        if "ignore previous instructions" in v.lower():
            raise ValueError("Potential injection attempt detected")
        return v

class ChatResponse(BaseModel):
    response_id: str
    content: str
    safety_flag: bool = Field(default=False)
    triggered_topic: Optional[str] = None

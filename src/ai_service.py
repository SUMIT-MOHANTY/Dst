import os
import openai
from .schemas import ChatRequest, ChatResponse
from .prompt_strategy import build_prompt

class AIService:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def generate_response(self, request: ChatRequest) -> ChatResponse:
        # Validate input via Pydantic model (Done in API layer, implied here)
        system_prompt = build_prompt(request.user_query)
        
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": request.user_query}
                ],
                temperature=0.2
            )
            
            reply = completion.choices[0].message.content
            return ChatResponse(
                response_id="resp_123", 
                content=reply, 
                safety_flag=False
            )
        except Exception as e:
            return ChatResponse(
                response_id="error", 
                content="I'm sorry, I cannot process that request.", 
                safety_flag=True
            )

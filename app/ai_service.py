from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def get_completion(prompt: str, temperature: float = 0.7):
    try:
        response = client.chat.completions.create(
            model=settings.AI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"AI Service Error: {str(e)}")

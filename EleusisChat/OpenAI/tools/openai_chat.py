import openai
import os
from logger import logger

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        logger.error(f"Failed to generate OpenAI response: {e}")
        raise

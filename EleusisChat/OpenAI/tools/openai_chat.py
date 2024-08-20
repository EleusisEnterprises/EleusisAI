import openai
import os
from logger import logger

# Ensure the API key is loaded correctly
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    try:
        logger.info(f"Sending prompt to OpenAI: {prompt}")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1000
        )
        logger.info(f"OpenAI response: {response}")
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        logger.error(f"OpenAI API error: {e}")
        raise
    except Exception as e:
        logger.error(f"General error in generate_response: {e}")
        raise

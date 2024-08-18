import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Specify the model you want to use
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150
    )
    return response['choices'][0]['message']['content']

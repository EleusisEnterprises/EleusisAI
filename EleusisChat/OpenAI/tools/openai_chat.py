import openai
from config import get_config
from logger import logger

# Load the configuration
config = get_config()

# Set up the OpenAI API key
openai.api_key = config.OPENAI_API_KEY

def generate_response(prompt):
    try:
        # Log the incoming prompt
        logger.info(f"Generating response for prompt: {prompt}")
        
        # Make a call to OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,  # You can adjust this value based on your needs
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the text from the response
        message = response.choices[0].message['content'].strip()

        # Log the generated response
        logger.info(f"Generated response: {message}")
        
        return message

    except Exception as e:
        logger.error(f"Failed to generate response: {str(e)}")
        return f"An error occurred: {str(e)}"

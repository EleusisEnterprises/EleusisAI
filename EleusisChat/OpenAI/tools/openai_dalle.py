# openai_dalle.py
import openai
from config import get_config
from logger import logger

# Load the configuration
config = get_config()

# Set up the OpenAI API key
openai.api_key = config.OPENAI_API_KEY

def generate_dalle_image(prompt, size="1024x1024"):
    try:
        # Log the incoming prompt
        logger.info(f"Generating DALL·E image for prompt: {prompt}")

        # Make a call to OpenAI API to generate an image
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=size  # Adjust the size as needed (e.g., "512x512", "1024x1024")
        )

        # Extract the URL of the generated image
        image_url = response['data'][0]['url']

        # Log the generated image URL
        logger.info(f"Generated DALL·E image URL: {image_url}")
        
        return image_url

    except Exception as e:
        logger.error(f"Failed to generate DALL·E image: {str(e)}")
        return f"An error occurred: {str(e)}"

import openai
import requests
from PIL import Image
from io import BytesIO
from config import get_config
from logger import logger
from flask import send_file

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
            size=size
        )

        # Extract the URL of the generated image
        image_url = response['data'][0]['url']
        logger.info(f"Received image URL: {image_url}")

        # Instead of downloading, return the image URL
        return image_url

    except requests.exceptions.RequestException as re:
        logger.error(f"HTTP request failed: {str(re)}")
    except openai.error.OpenAIError as oe:
        logger.error(f"OpenAI API error: {str(oe)}")
    except Exception as e:
        logger.error(f"Failed to generate DALL·E image: {str(e)}")
    return None

import openai
import requests
from PIL import Image
from io import BytesIO
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
            size=size
        )

        # Extract the URL of the generated image
        image_url = response['data'][0]['url']

        # Download the image
        image_response = requests.get(image_url)
        img = Image.open(BytesIO(image_response.content))

        # Convert the image to PNG format
        png_image = BytesIO()
        img.save(png_image, format='PNG')
        png_image.seek(0)  # Move to the beginning of the file

        # Log the generated image URL
        logger.info(f"Generated DALL·E image URL: {image_url}")
        
        return png_image

    except Exception as e:
        logger.error(f"Failed to generate DALL·E image: {str(e)}")
        return None

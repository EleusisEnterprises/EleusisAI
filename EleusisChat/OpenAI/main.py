from flask import Flask, request, jsonify
from tools.openai_chat import generate_response
from tools.openai_dalle import generate_dalle_image
import time
from logger import logger
from config import get_config
import requests
from io import BytesIO
from PIL import Image

# Load the configuration
config = get_config()

app = Flask(__name__)
app.config.from_object(config)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.json
        prompt = data.get('prompt')
        
        if not prompt:
            logger.error("Prompt is missing from the request")
            return jsonify({'error': 'Prompt is required'}), 400

        logger.info(f"Received prompt: {prompt}")
        response = generate_response(prompt)
        logger.info(f"Generated response: {response}")
        return jsonify({'response': response})

    except Exception as e:
        logger.error(f"Failed to process prompt: {str(e)}")
        return jsonify({'error': f"Failed to process prompt: {str(e)}"}), 500

@app.route('/generate-image', methods=['POST'])
def generate_image():
    try:
        data = request.json
        prompt = data.get('prompt')
        size = data.get('size', '1024x1024')  # Optional, defaults to 1024x1024

        if not prompt:
            logger.error("Prompt is missing from the request")
            return jsonify({'error': 'Prompt is required'}), 400

        logger.info(f"Received prompt for DALL·E: {prompt}")
        image_url = generate_dalle_image(prompt, size)
        logger.info(f"Generated DALL·E image URL: {image_url}")
        return jsonify({'image_url': image_url})

    except Exception as e:
        logger.error(f"Failed to generate image: {str(e)}")
        return jsonify({'error': f"Failed to generate image: {str(e)}"}), 500
    
@app.route('/generate-image', methods=['POST'])
def generate_image():
    try:
        data = request.json
        prompt = data.get('prompt')
        size = data.get('size', '1024x1024')  # Optional, defaults to 1024x1024

        if not prompt:
            logger.error("Prompt is missing from the request")
            return jsonify({'error': 'Prompt is required'}), 400

        logger.info(f"Received prompt for DALL·E: {prompt}")
        return generate_dalle_image(prompt, size)

    except Exception as e:
        logger.error(f"Failed to generate image: {str(e)}")
        return jsonify({'error': f"Failed to generate image: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

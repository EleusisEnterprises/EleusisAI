import pytesseract
import cv2
from flask import Flask, request, jsonify
from tools.langchain_tools import create_analysis_chain
from tools.data_extraction import extract_data_from_image
from tools.ta_tools import calculate_technical_indicators, generate_analysis_prompt
from tools.openai_chat import generate_response
from logger import logger
import requests
import os
from config import get_config

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

def download_image(image_url):
    """
    Download an image from a given URL and save it locally.
    """
    try:
        response = requests.get(image_url)
        response.raise_for_status()

        if not os.path.exists('images'):
            os.makedirs('images')

        image_path = os.path.join('images', os.path.basename(image_url))
        with open(image_path, 'wb') as f:
            f.write(response.content)

        logger.info(f"Image downloaded to: {image_path}")
        return image_path

    except Exception as e:
        logger.error(f"Failed to download image: {str(e)}")
        raise

@app.route('/analyse', methods=['POST'])
def analyse():
    """
    Endpoint to handle image analysis requests.
    """
    try:
        data = request.json
        image_url = data.get('image_url', '')

        if not image_url:
            logger.error("Image URL is missing from the request")
            return jsonify({'error': 'Image URL is required'}), 400

        logger.info(f"Received image URL: {image_url}")
        image_path = download_image(image_url)

        # Extract data from the image
        df = extract_data_from_image(image_path)
        logger.info(f"Extracted data: {df}")

        # Perform technical analysis with your specified settings
        df = calculate_technical_indicators(df)
        logger.info(f"Calculated technical indicators: {df}")

        # Generate analysis prompt
        prompt = generate_analysis_prompt(df)
        logger.info(f"Generated analysis prompt: {prompt}")

        # Generate the summary using GPT-4
        summary = generate_response(prompt)
        logger.info(f"Generated summary: {summary}")

        return jsonify({'response': summary})

    except Exception as e:
        logger.error(f"Failed to analyze image: {str(e)}")
        return jsonify({'error': f"Failed to analyze image: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

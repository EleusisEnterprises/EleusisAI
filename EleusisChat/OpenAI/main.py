from flask import Flask, request, jsonify
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

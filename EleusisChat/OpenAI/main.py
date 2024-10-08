import logging
from flask import Flask, request, jsonify
from tools.openai_chat import generate_response
from tools.openai_dalle import generate_dalle_image
from tools.conversational_mem import create_elly_message, create_user_message, link_messages
from py2neo import Graph
import os
from config import get_config
from datetime import datetime
import time

# Load the configuration
config = get_config()

app = Flask(__name__)
app.config.from_object(config)

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level
logger = logging.getLogger(__name__)

def connect_to_neo4j(retries=0, delay=5):
    """
    Attempts to connect to the Neo4j database.
    Retries the connection attempt if it fails, up to a maximum number of retries.
    
    Args:
        retries (int): Number of times to retry the connection if it fails. Default is 5.
        delay (int): Number of seconds to wait between retries. Default is 5 seconds.
        
    Returns:
        Graph: Neo4j Graph object if the connection is successful.
        None: If the connection fails after the specified number of retries.
    """
    attempt = 0
    while attempt < retries:
        try:
            # Attempt to connect to Neo4j
            graph = Graph(os.getenv("NEO4J_URI"), auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD")))
            # Test the connection by running a simple query
            graph.run("RETURN 1")
            logger.info("Connected to Neo4j successfully.")
            return graph
        except Exception as e:
            attempt += 1
            logger.error(f"Attempt {attempt}/{retries} - Failed to connect to Neo4j: {str(e)}")
            time.sleep(delay)
    
    logger.error("Exceeded maximum retry attempts. Could not connect to Neo4j.")
    return None

# Connect to Neo4j with retry logic
graph = connect_to_neo4j(retries=50, delay=10)  # Adjust retries and delay as needed

@app.route('/ask', methods=['POST'])
def ask():
    if not graph:
        return jsonify({'error': 'Neo4j is not connected'}), 500
    
    try:
        data = request.json
        prompt = data.get('prompt')
        
        if not prompt:
            logger.error("Prompt is missing from the request")
            return jsonify({'error': 'Prompt is required'}), 400

        logger.info(f"Received prompt: {prompt}")

        # Create and store the user message
        user_message = create_user_message(prompt)

        # Generate the response from Elly
        elly_response = generate_response(prompt)
        elly_message = create_elly_message(elly_response)

        # Link the user message to the Elly response
        link_messages(user_message, elly_message)

        return jsonify({'response': elly_response})

    except Exception as e:
        logger.error(f"Failed to process prompt: {str(e)}")
        return jsonify({'error': f"Failed to process prompt: {str(e)}"}), 500

@app.route('/generate-image', methods=['POST'])
def generate_image():
    if not graph:
        return jsonify({'error': 'Neo4j is not connected'}), 500

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

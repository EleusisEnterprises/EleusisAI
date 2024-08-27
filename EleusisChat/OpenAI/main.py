import logging
from flask import Flask, request, jsonify
from tools.openai_chat import generate_response
from tools.openai_dalle import generate_dalle_image
from tools.mindpalace_tools import create_user_note, create_ai_note, create_message_chain, link_notes
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

def connect_to_neo4j(retries=20, delay=5):
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
graph = connect_to_neo4j(retries=10, delay=5)  # Adjust retries and delay as needed


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

        # Create a user note for the prompt
        user_note = create_user_note(prompt)

        # Check for existing context in the Zettelkasten
        context_query = """
        MATCH (n:Note)
        WHERE n.title CONTAINS $prompt OR n.content CONTAINS $prompt
        RETURN n.title, n.content
        LIMIT 5
        """
        context = graph.run(context_query, prompt=prompt).data()

        if context:
            # If context exists, create a context-aware prompt
            context_summary = "\n".join([f"{n['n.title']}: {n['n.content']}" for n in context])
            enhanced_prompt = f"Based on the following information, {context_summary}, please answer: {prompt}"
            ai_note = create_ai_note(enhanced_prompt)
            logger.info(f"Generated context-aware response: {ai_note['content']}")

            # Link new response to existing notes
            for note in context:
                link_notes(ai_note['title'], note['n.title'], "CONTEXT_OF")

        else:
            # No context exists, generate a fresh response
            ai_note = create_ai_note(prompt)
            logger.info(f"Generated response without context: {ai_note['content']}")

        # Create the conversation chain by linking the user note and AI note
        create_message_chain(user_note, ai_note)

        return jsonify({'response': ai_note['content']})

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

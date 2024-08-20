import openai
import os
from logger import logger
from MindPalace.app.db import Neo4jDatabase  # Update this line

# Initialize the Neo4j database connection
db = Neo4jDatabase()

# Ensure the API key is loaded correctly
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_neo4j_command(response):
    # Extract the Neo4j command from the GPT-4 response
    command_start = response.find("NEO4J_COMMAND:")
    if command_start != -1:
        command_end = response.find("\n", command_start)
        command = response[command_start + len("NEO4J_COMMAND:"):command_end].strip()
        return command
    else:
        raise ValueError("No Neo4j command found in the response.")

def generate_response(prompt):
    try:
        logger.info(f"Sending prompt to OpenAI: {prompt}")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1000
        )
        result = response['choices'][0]['message']['content']

        # Check if the response suggests an action with Neo4j
        if "NEO4J_COMMAND:" in result:
            # Parse and execute a Neo4j command, e.g., add a node or query
            neo4j_command = extract_neo4j_command(result)
            db.run_query(neo4j_command)
            logger.info(f"Executed Neo4j command: {neo4j_command}")

        return result
    except openai.error.OpenAIError as e:
        logger.error(f"OpenAI API error: {e}")
        raise
    except Exception as e:
        logger.error(f"General error in generate_response: {e}")
        raise

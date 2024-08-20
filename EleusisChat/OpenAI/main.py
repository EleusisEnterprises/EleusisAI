from flask import Flask, request, jsonify
from tools.openai_chat import generate_response
from MindPalace.app.db import Neo4jDatabase
from logger import logger
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
    
# Initialize Neo4j database connection
db = Neo4jDatabase()

@app.route('/query', methods=['POST'])
def query_neo4j():
    try:
        query = request.json.get('query')
        if not query:
            return jsonify({'error': 'Query is required'}), 400
        
        result = db.run_query(query)
        return jsonify({'result': result}), 200
    except Exception as e:
        logger.error(f"Failed to execute query: {str(e)}")
        return jsonify({'error': f"Failed to execute query: {str(e)}"}), 500

@app.route('/add-node', methods=['POST'])
def add_node():
    try:
        node_data = request.json.get('node_data')
        if not node_data:
            return jsonify({'error': 'Node data is required'}), 400
        
        query = f"CREATE (n:{node_data['label']} {{name: '{node_data['name']}', description: '{node_data['description']}'}})"
        db.run_query(query)
        return jsonify({'message': 'Node added successfully'}), 200
    except Exception as e:
        logger.error(f"Failed to add node: {str(e)}")
        return jsonify({'error': f"Failed to add node: {str(e)}"}), 500

@app.route('/update-node', methods=['POST'])
def update_node():
    try:
        node_id = request.json.get('node_id')
        update_data = request.json.get('update_data')
        if not node_id or not update_data:
            return jsonify({'error': 'Node ID and update data are required'}), 400
        
        query = f"MATCH (n) WHERE ID(n) = {node_id} SET n += {update_data}"
        db.run_query(query)
        return jsonify({'message': 'Node updated successfully'}), 200
    except Exception as e:
        logger.error(f"Failed to update node: {str(e)}")
        return jsonify({'error': f"Failed to update node: {str(e)}"}), 500

@app.route('/delete-node', methods=['DELETE'])
def delete_node():
    try:
        node_id = request.json.get('node_id')
        if not node_id:
            return jsonify({'error': 'Node ID is required'}), 400
        
        query = f"MATCH (n) WHERE ID(n) = {node_id} DELETE n"
        db.run_query(query)
        return jsonify({'message': 'Node deleted successfully'}), 200
    except Exception as e:
        logger.error(f"Failed to delete node: {str(e)}")
        return jsonify({'error': f"Failed to delete node: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

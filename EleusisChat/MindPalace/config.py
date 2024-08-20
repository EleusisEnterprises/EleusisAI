import os
from dotenv import load_dotenv

# Option 1: Using raw string
# load_dotenv(r'C:\Users\corey\EleusisAI\EleusisChat\.env')

# Option 2: Using forward slashes
# load_dotenv('C:/Users/corey/EleusisAI/EleusisChat/.env')

# Option 3: Escaping backslashes
load_dotenv('C:\\Users\\corey\\EleusisAI\\EleusisChat\\.env')

class Config:
    NEO4J_URI = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
    NEO4J_USER = os.getenv('NEO4J_USER', 'neo4j')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD', 'password')  # Replace with actual default password

config = Config()

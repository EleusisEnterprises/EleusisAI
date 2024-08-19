import os
from dotenv import load_dotenv

# Load environment variables from the specified .env file
env_path = os.path.join('..', 'EleusisChat', '.env')
load_dotenv(dotenv_path=env_path)

# Assign environment variables to Python variables
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

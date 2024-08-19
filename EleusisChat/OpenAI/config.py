import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def get_config():
    return Config()

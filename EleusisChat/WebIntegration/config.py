import os

# Directly define SERPAPI_KEY from environment variable
SERPAPI_KEY = os.getenv('SERPAPI_KEY')

class Config:
    SERPAPI_KEY = os.getenv('SERPAPI_KEY')


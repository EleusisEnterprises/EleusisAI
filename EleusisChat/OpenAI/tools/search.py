import requests
from config import get_config
from logger import logger

# Load the configuration
config = get_config()

def search_google(query):
    try:
        # Format the query appropriately
        search_query = query.replace("look up", "").replace("search for", "").replace("find information on", "").strip()
        
        params = {
            "q": search_query,
            "hl": "en",
            "gl": "us",
            "api_key": config.SERPAPI_KEY
        }

        response = requests.get("https://serpapi.com/search", params=params)
        results = response.json()

        if 'organic_results' in results:
            search_results = ""
            for result in results['organic_results']:
                search_results += f"**{result['title']}**\n{result['link']}\n\n"
            return search_results
        else:
            logger.error("No organic results found or an error occurred in the API response")
            return "No search results found."

    except Exception as e:
        logger.error(f"Failed to perform search: {str(e)}")
        return f"An error occurred during the search: {str(e)}"

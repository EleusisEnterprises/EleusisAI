import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from logger import logger
from config import Config  # Import the Config class to get the SERPAPI_KEY

# Access the SERPAPI_KEY from the config file
SERPAPI_KEY = Config.SERPAPI_KEY

# Function to perform a Google search using SerpAPI
def perform_search(query):
    try:
        params = {
            "q": query,
            "hl": "en",
            "gl": "us",
            "api_key": SERPAPI_KEY
        }
        response = requests.get("https://serpapi.com/search", params=params)
        results = response.json()

        if 'organic_results' in results:
            urls = [result['link'] for result in results['organic_results']]
            return urls
        else:
            logger.error("No organic results found.")
            return []

    except Exception as e:
        logger.error(f"Failed to perform search: {str(e)}")
        return []

# Function to scrape a website using BeautifulSoup
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# Function to load dynamic content using Selenium
def load_dynamic_content(url):
    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    driver.quit()
    return soup

# Main function to run the entire process
def main():
    query = "your search query"
    
    # Perform Google search using SerpAPI
    search_results = perform_search(query)
    
    if not search_results:
        logger.error("No results found or failed to perform search.")
        return

    # Extract URLs from search results
    for url in search_results:
        # Scrape static content
        soup = scrape_website(url)
        print(f"Title from BeautifulSoup: {soup.title.text}")
        
        # Optionally load dynamic content
        soup_dynamic = load_dynamic_content(url)
        print(f"Title from Selenium: {soup_dynamic.title.text}")

if __name__ == "__main__":
    main()

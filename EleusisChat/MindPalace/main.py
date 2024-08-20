from app.db import Neo4jDatabase
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Initialize the Neo4j database connection
    logger.info("Initializing Neo4j database connection...")
    db = Neo4jDatabase()

    # Check the connection by running a simple query
    try:
        logger.info("Running a test query...")
        result = db.run_query("MATCH (n) RETURN COUNT(n)")
        logger.info(f"Database connected successfully. Number of nodes: {result}")
    except Exception as e:
        logger.error(f"Error connecting to the database: {e}")
        return

    # Placeholder for additional logic
    logger.info("MindPalace service is up and running!")

    # Keep the service running
    while True:
        time.sleep(3600)  # Sleep for 1 hour, keeping the service alive

if __name__ == "__main__":
    main()

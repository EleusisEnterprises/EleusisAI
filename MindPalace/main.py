# main.py (or wherever you're initializing the Neo4j connection)

from neo4j import GraphDatabase
import config

class Zettelkasten:

    def __init__(self):
        self.driver = GraphDatabase.driver(config.NEO4J_URI, auth=(config.NEO4J_USER, config.NEO4J_PASSWORD))

    def close(self):
        self.driver.close()

    # Define methods for creating and linking notes...

# Initialize the Zettelkasten with the configuration
zettel = Zettelkasten()

# Example usage
# zettel.create_note("1", "This is the first note.")
# zettel.create_note("2", "This is the second note, related to the first.")
# zettel.link_notes("1", "2", "SUPPORTS")

# zettel.close()

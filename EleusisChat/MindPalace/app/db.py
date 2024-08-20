from neo4j import GraphDatabase
from app import config, db
# Update this line

class Neo4jDatabase:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            config.NEO4J_URI, 
            auth=(config.NEO4J_USER, config.NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def run_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return result.data()

# Example usage
if __name__ == "__main__":
    db = Neo4jDatabase()
    result = db.run_query("MATCH (n) RETURN n LIMIT 1")
    print(result)
    db.close()

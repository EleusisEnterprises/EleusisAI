from neo4j import GraphDatabase
import os
import dotenv as getenv

uri = os.getenv("NEO4J_URI", "bolt://neo4j:7687")
user = os.getenv("NEO4J_USER", "neo4j")
password = os.getenv("NEO4J_PASSWORD", "password")

driver = GraphDatabase.driver(uri, auth=(user, password))

def test_connection():
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN COUNT(n) AS count")
        count = result.single().get("count")
        print(f"Number of nodes in the database: {count}")

if __name__ == "__main__":
    try:
        test_connection()
        print("Connection to Neo4j was successful.")
    except Exception as e:
        print(f"Connection failed: {e}")

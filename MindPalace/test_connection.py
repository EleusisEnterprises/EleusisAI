from neo4j import GraphDatabase
import config

def test_connection():
    try:
        driver = GraphDatabase.driver(config.NEO4J_URI, auth=(config.NEO4J_USER, config.NEO4J_PASSWORD))
        with driver.session() as session:
            result = session.run("RETURN 1")
            print("Connection successful:", result.single()[0] == 1)
    except Exception as e:
        print("Connection failed:", str(e))
    finally:
        driver.close()

if __name__ == "__main__":
    test_connection()

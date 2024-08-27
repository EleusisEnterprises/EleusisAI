from py2neo import Graph, Node, Relationship
from tools.openai_chat import generate_response
import os
from datetime import datetime  # Import the datetime module
import logging

logger = logging.getLogger(__name__)

# Connect to Neo4j
graph = Graph(os.getenv("NEO4J_URI"), auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD")))

def create_user_note(prompt):
    user_note = Node("Note", title=prompt, content=prompt, created_at=datetime.now().isoformat())
    graph.create(user_note)
    logger.info(f"User note created with title: '{prompt}' and saved to Neo4j.")
    return user_note

def create_ai_note(prompt):
    content = generate_response(prompt)
    ai_note = Node("Note", title=f"Response to: {prompt}", content=content, created_at=datetime.now().isoformat())
    graph.create(ai_note)
    logger.info(f"AI note created for prompt: '{prompt}' with content: '{content}' and saved to Neo4j.")
    return ai_note

def create_message_chain(user_note, ai_note):
    graph.create(Relationship(user_note, "ASKED_FOR", ai_note))
    logger.info(f"Message chain created between user note '{user_note['title']}' and AI note '{ai_note['title']}'.")
    return user_note, ai_note

def link_notes(note_title, related_note_title, relationship_type="RELATED_TO"):
    query = """
    MATCH (a:Note), (b:Note)
    WHERE a.title = $note_title AND b.title = $related_note_title
    CREATE (a)-[r:%s]->(b)
    RETURN type(r)
    """ % relationship_type
    
    result = graph.run(query, note_title=note_title, related_note_title=related_note_title).data()
    logger.info(f"Linked note '{note_title}' to '{related_note_title}' with relationship '{relationship_type}'.")
    return result

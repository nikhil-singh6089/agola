from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
import json
from typing import Dict, Any

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

def neo4j_to_json(driver):
    nodes = {}
    edges = []

    with driver.session() as session:
        # Fetch all nodes
        result = session.run("MATCH (n) RETURN n")
        for record in result:
            node = record['n']
            node_id = node.element_id.split(':')[-1]
            node_label = list(node.labels)[0] if node.labels else 'Node'
            node_name = node.get('id', node_id)
            nodes[node_id] = {'id': node_id, 'label': f"{node_label}: {node_name}", 'properties': dict(node)}

        # Fetch all relationships
        result = session.run("MATCH ()-[r]->() RETURN r")
        for record in result:
            rel = record['r']
            source_id = rel.start_node.element_id.split(':')[-1]
            target_id = rel.end_node.element_id.split(':')[-1]
            edges.append({
                'source': source_id,
                'target': target_id,
                'label': rel.type,
                'properties': dict(rel)
            })

    return {
        'nodes': list(nodes.values()),
        'edges': edges
    }



# # Example Cypher query
# cypher_query = """
# MATCH (n)
# OPTIONAL MATCH (n)-[r]->(m)
# RETURN n, r, m
# """


def get_neo4j_data() -> Dict[str, Any]:
    try:
        with GraphDatabase.driver(NEO4J_URI, auth=('neo4j', NEO4J_PASSWORD)) as driver:
            graph_data = neo4j_to_json(driver)

        # # Convert to JSON string
        # json_data = json.dumps(graph_data, indent=2)

        # print(json_data)
        return graph_data
        # # Optionally, save to a file
        # with open('graph_data.json', 'w') as f:
        #     f.write(json_data)
    except Exception as e:
        # Log the error or handle it as appropriate for your application
        print(f"An error occurred: {e}")
        return {"error": str(e)}


# <Record 
# n=<Node element_id='4:891e89a5-b2d6-46c0-b62f-c7904744e359:0' labels=frozenset({'System'}) properties={'id': 'Student’S Attendance System'}> 
# r=<Relationship element_id='5:891e89a5-b2d6-46c0-b62f-c7904744e359:1152924803141730304' 
#   nodes=(<Node element_id='4:891e89a5-b2d6-46c0-b62f-c7904744e359:0' labels=frozenset({'System'}) properties={'id': 'Student’S Attendance System'}>, 
#          <Node element_id='4:891e89a5-b2d6-46c0-b62f-c7904744e359:4' labels=frozenset({'Person'}) properties={'id': 'Faculty'}>) 
#           type='PROVIDES_ACCESS_TO' properties={}> 
# m=<Node element_id='4:891e89a5-b2d6-46c0-b62f-c7904744e359:4' labels=frozenset({'Person'}) properties={'id': 'Faculty'}>
# >



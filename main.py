import pandas as pd
from langchain_neo4j import Neo4jGraph

df = pd.read_csv("imdb.csv")
df = df.drop(
    columns=["Poster_Link", "Certificate", "No_of_Votes", "Overview", "Runtime"]
)

# Replace with your actual key if needed


URI = "neo4j+s://ac932081.databases.neo4j.io"
AUTH = ("ac932081", "6vzDNF3_A0ocOzkjv8kGrl_koVzcXSY6FgdBuHGzz50")

graph = Neo4jGraph(url=URI, username=AUTH[0], password=AUTH[1], database="ac932081")


cypher_query = """
MERGE (m:Movie {title: $title})
MERGE (d:Director {name: $director})
MERGE (a:Actor {name: $star1})
MERGE (b:Actor {name: $star2})
MERGE (c:Actor {name: $star3})
MERGE (g:Genre {name: $genre})
MERGE (m)-[:DIRECTED_BY]->(d)
MERGE (m)-[:HAS_ACTOR]->(a)
MERGE (m)-[:HAS_ACTOR]->(b)
MERGE (m)-[:HAS_ACTOR]->(c)
MERGE (m)-[:HAS_GENRE]->(g)
"""

for index, row in df.iterrows():
    params = {
        "title": str(row["Series_Title"]),
        "director": str(row["Director"]),
        "star1": str(row["Star1"]),
        "star2": str(row["Star2"]),
        "star3": str(row["Star3"]),
        "genre": str(row["Genre"]),
    }
    graph.query(cypher_query, params=params)

graph.refresh_schema()

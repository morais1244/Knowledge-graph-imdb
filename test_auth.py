from neo4j import GraphDatabase

URI = "neo4j+s://ac932081.databases.neo4j.io"
passw = "6vzDNF3_A0ocOzkjv8kGrl_koVzcXSY6FgdBuHGzz50"

print("Testing with neo4j...")
try:
    with GraphDatabase.driver(URI, auth=("neo4j", passw)) as driver:
        driver.verify_connectivity()
    print("neo4j user SUCCESS")
except Exception as e:
    print(f"neo4j user FAILED: {type(e).__name__} - {e}")

print("Testing with ac932081...")
try:
    with GraphDatabase.driver(URI, auth=("ac932081", passw)) as driver:
        driver.verify_connectivity()
    print("ac932081 user SUCCESS")
except Exception as e:
    print(f"ac932081 user FAILED: {type(e).__name__} - {e}")

import os

from langchain_neo4j import GraphCypherQAChain, Neo4jGraph
from langchain_openai import ChatOpenAI

API_KEY = "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"
os.environ["OPENROUTER_API_KEY"] = API_KEY
URI = "neo4j+s://ac932081.databases.neo4j.io"
AUTH = ("ac932081", "6vzDNF3_A0ocOzkjv8kGrl_koVzcXSY6FgdBuHGzz50")

print("A conectar ao Grafo no Neo4j...")
graph = Neo4jGraph(url=URI, username=AUTH[0], password=AUTH[1], database="ac932081")

graph.refresh_schema()
print("Conexão estabelecida com sucesso!")

llm = ChatOpenAI(
    openai_api_key=API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",  # URL essencial do OpenRouter
    model_name="deepseek/deepseek-r1-0528",  # Nome do modelo no OpenRouter
    temperature=0,
    max_tokens=500,
)

chain = GraphCypherQAChain.from_llm(
    cypher_llm=llm,
    qa_llm=llm,
    graph=graph,
    verbose=True,
    allow_dangerous_requests=True,
)

print(graph.schema)
while True:
    pergunta = input(
        "\nFaça uma pergunta sobre os filmes (ou digite 'sair' para encerrar): "
    )

    if pergunta.lower() == "sair":
        break

    try:
        # O sistema processa a pergunta e busca no Neo4j
        resposta = chain.invoke({"query": pergunta})
        print(f"\n🤖 Resposta: {resposta['result']}")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro ao processar a pergunta: {e}")

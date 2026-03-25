import os

from neo4j import GraphDatabase
from pyvis.network import Network

# ==========================================
# 1. CONFIGURAÇÕES E CONEXÃO COM O NEO4J
# ==========================================
# Use as mesmas credenciais do seu projeto

URI = "neo4j+s://ac932081.databases.neo4j.io"
AUTH = ("ac932081", "6vzDNF3_A0ocOzkjv8kGrl_koVzcXSY6FgdBuHGzz50")
# Criar o driver de conexão
driver = GraphDatabase.driver(URI, auth=(AUTH[0], AUTH[1]))

# ==========================================
# 2. INICIALIZAR A REDE PYVIS
# ==========================================
# Criamos uma rede de visualização interativa
# Pode ajustar a altura e o fundo
net = Network(
    height="100vh", width="100%", bgcolor="#222222", font_color="white", directed=True
)

# Adicionar opções de interação (basta clicar no botão no HTML gerado)
net.show_buttons(filter_=["physics"])

# ==========================================
# 3. CONSULTAR O NEO4J E EXTRAIR DADOS
# ==========================================
# Consulta Cypher para pegar numa amostra do grafo
# LIMITAMOS a 150 para a visualização não ficar muito lenta
query = """
MATCH (n)-[r]->(m)
RETURN n, r, m
LIMIT 150
"""

print("A conectar ao Neo4j e a extrair dados...")
with driver.session() as session:
    result = session.run(query)

    # Iterar sobre os resultados brutos da consulta
    for record in result:
        node_n = record["n"]
        node_m = record["m"]
        rel_r = record["r"]

        # --- Processar Nó de Origem (n) ---
        id_n = node_n.id
        # Define o rótulo (título ou nome) e a cor baseada no tipo (Label)
        label_n = node_n.get("titulo") or node_n.get("nome") or str(id_n)

        color_n = (
            "blue"
            if "Filme" in node_n.labels
            else "green"
            if "Pessoa" in node_n.labels
            else "red"
        )
        # O título aparece ao passar o rato por cima
        net.add_node(
            id_n,
            label=label_n,
            color=color_n,
            title=f"Labels: {node_n.labels}\nProps: {dict(node_n)}",
        )

        # --- Processar Nó de Destino (m) ---
        id_m = node_m.id
        label_m = node_m.get("titulo") or node_m.get("nome") or str(id_m)
        color_m = (
            "blue"
            if "Filme" in node_m.labels
            else "green"
            if "Pessoa" in node_m.labels
            else "red"
        )
        net.add_node(
            id_m,
            label=label_m,
            color=color_m,
            title=f"Labels: {node_m.labels}\nProps: {dict(node_m)}",
        )

        # --- Processar Aresta/Relação (r) ---
        type_r = rel_r.type
        # Conecta o nó de origem ao de destino com o tipo de relação
        net.add_edge(id_n, id_m, label=type_r, title=type_r)

# Fechar o driver do Neo4j
driver.close()

# ==========================================
# 4. GERAR E MOSTRAR O GRAFO
# ==========================================
# Define o nome do ficheiro HTML que será gerado
nome_ficheiro = "grafo_imdb_interativo.html"
print(f"Grafo gerado com sucesso! Abra o ficheiro '{nome_ficheiro}' no seu navegador.")

# Salva o grafo num ficheiro HTML e abre-o automaticamente no navegador padrão
net.write_html(nome_ficheiro)

# Knowledge Graph IMDB 🎬🕸️

Este projeto constrói um **Grafo de Conhecimento (Knowledge Graph)** a partir de uma base de dados de filmes do IMDB e permite que o usuário faça consultas em linguagem natural utilizando Inteligência Artificial (LLMs) via Langchain.

## 🚀 Funcionalidades

1. **Processamento de Dados:** Lê o arquivo `imdb.csv` usando Pandas e limpa colunas desnecessárias.
2. **Criação do Grafo (Neo4j):** Mapeia os dados estruturados para um banco de dados em grafos (Neo4j AuraDB), criando os seguintes nós e relacionamentos:
   - **Nós:** `Movie` (Filme), `Director` (Diretor), `Actor` (Ator), `Genre` (Gênero).
   - **Relacionamentos:** `DIRECTED_BY` (Dirigido por), `HAS_ACTOR` (Tem ator), `HAS_GENRE` (Tem gênero).
3. **Consulta em Linguagem Natural (QA):** Utiliza LLMs (OpenAI GPT-4o-mini ou Google Gemini) com Langchain (`GraphCypherQAChain`) para traduzir perguntas feitas em português/inglês direto para linguagem de consulta do Neo4j (Cypher), retornando a resposta exata ao usuário.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Banco de Dados:** Neo4j (AuraDB - Cloud)
- **Bibliotecas Principais:**
  - `pandas` (Manipulação de dados)
  - `neo4j` (Driver oficial)
  - `langchain_neo4j` (Integração de Grafos no Langchain)
  - `langchain_openai` / `langchain_google_genai` (Modelos LLM)

## 📁 Estrutura do Projeto

- `imdb.csv`: Dataset contendo as informações dos filmes.
- `main.py`: Script responsável por ler o CSV e popular o banco de dados Neo4j construindo o Grafo.
- `consult.py`: Script interativo de Chatbot no terminal para conversar e fazer perguntas sobre os filmes do banco.

## ⚙️ Como Configurar e Executar

### 1. Pré-requisitos
- Ter o Python instalado.
- Ter uma conta no [Neo4j Aura](https://neo4j.com/cloud/platform/aura-graph-database/) e criar uma instância Free. Guarde a `URI`, `Username` e `Password`.
- Ter uma API Key da OpenAI (`OPENAI_API_KEY`) ou do Google Gemini (`GOOGLE_API_KEY`).

### 2. Instalação
Clone este repositório e instale as dependências. Recomenda-se o uso de um ambiente virtual:

```bash
python -m venv ambiente
source ambiente/bin/activate  # No Linux/Mac
# ambiente\Scripts\activate   # No Windows

pip install pandas neo4j langchain-neo4j langchain-openai langchain-google-genai
```

### 3. Configurando as Credenciais
Antes de executar os scripts, atualize as variáveis de ambiente dentro de `main.py` e `consult.py` com as suas chaves e credenciais reais:

```python
URI = "neo4j+s://<sua-instancia>.databases.neo4j.io"
AUTH = ("<seu-usuario>", "<sua-senha>")
```
E configure a sua chave da OpenAI ou Google conforme o modelo escolhido no script.

### 4. Populando o Banco de Dados
Execute o script principal para ler o arquivo `imdb.csv` e enviar os nós e relacionamentos para o seu banco Neo4j. Isso pode demorar alguns minutos dependendo do tamanho do dataset:

```bash
python main.py
```

### 5. Consultando os Dados (Chat)
Após o banco de dados estar populado, execute o script de consulta para interagir com os seus dados fazendo perguntas normais (ex: *"Quem dirigiu o filme O Poderoso Chefão?"*, *"Quais filmes o ator X participou?"*):

```bash
python consult.py
```

from sqlalchemy import make_url
from llama_index.core import SimpleDirectoryReader, StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.postgres import PGVectorStore
import textwrap
import api_key
import openai
import psycopg2
from pathlib import Path


#load documents from datasets folder
root_path = Path(__file__).resolve().parent
file_path = root_path.joinpath("datasets", "SeguroDental")
documents = SimpleDirectoryReader(str(file_path)).load_data()


# db creation
connection_string = "postgresql://admin:Batman1@localhost:5432/postgres"
db_name = "vector_db_mapfre_g1"
conn = psycopg2.connect(connection_string)
conn.autocommit = True

with conn.cursor() as c:
    c.execute(f"DROP DATABASE IF EXISTS {db_name}")
    c.execute(f"CREATE DATABASE {db_name}")


# indexes generation
url = make_url(connection_string)
vector_store = PGVectorStore.from_params(
    database="vector_db_mapfre_g1",
    host="localhost",
    password="Batman1",
    port="5432",
    user="admin",
    table_name="test",
    embed_dim=1536,  # openai embedding dimension
)

storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, show_progress=True
)
query_engine = index.as_query_engine()

# import logging
# import sys

# Uncomment to see debug logs
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index.core import SimpleDirectoryReader, StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.postgres import PGVectorStore
import textwrap
import openai
from pathlib import Path


root_path = Path(__file__).resolve().parent
file_path = root_path.joinpath("datasets", "SeguroDental")
documents = SimpleDirectoryReader(str(file_path)).load_data()
print("Document ID:", documents[0].doc_id)


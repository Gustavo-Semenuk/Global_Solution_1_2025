# ms_chat_ai/models/supabase_store.py

from supabase import create_client
from langchain_community.vectorstores.supabase import SupabaseVectorStore
from langchain.embeddings import OllamaEmbeddings
from dotenv import load_dotenv
import os


# Carrega as variáveis do .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("As variáveis SUPABASE_URL e SUPABASE_KEY precisam estar definidas.")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# Função que retorna o vector store para uso no RAG
def get_supabase_vectorstore():
    embeddings = OllamaEmbeddings(model="llama3:instruct")
    vectorstore = SupabaseVectorStore(
        client=supabase,
        embedding=embeddings,
        table_name="documents"  # certifique-se que a tabela está criada
    )
    return vectorstore

__all__ = ["get_supabase_vectorstore"]
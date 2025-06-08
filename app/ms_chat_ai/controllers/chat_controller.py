# controllers/chat_controller.py
import os
from supabase import create_client, Client
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain_core.runnables import RunnableLambda
from ms_chat_ai.models.supabase_store import get_supabase_vectorstore
from ms_chat_ai.services.rag_service import run_rag


def chat_rag_response(user_query: str) -> dict:
    return run_rag(user_query)


# services/rag_service.py

# Configure LLM and Embeddings
llm = Ollama(model="llama3:instruct")
embeddings = OllamaEmbeddings(model="llama3:instruct")

# Use Supabase to load documents (already stored) and create retriever
vectorstore = Chroma(persist_directory="db", embedding_function=embeddings)
retriever = vectorstore.as_retriever()

# Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)


def get_rag_response(query: str) -> str:
    result = qa_chain({"query": query})
    return result["result"]


# models/supabase_store.py

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_supabase_docs():
    response = supabase.table("documents").select("*").execute()
    return response.data

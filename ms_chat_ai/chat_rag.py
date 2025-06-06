import streamlit as st
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import SupabaseVectorStore
from langchain.chat_models import ChatOllama
from langchain.chains import RetrievalQA
from langchain.schema import SystemMessage
from supabase import create_client
import os

# Configurações iniciais
SUPABASE_URL = "https://<sua-instancia>.supabase.co"
SUPABASE_KEY = "<sua-chave-secreta>"

# Criar cliente Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Streamlit - título
st.set_page_config(page_title="Chat RAG com Supabase", layout="wide")
st.title("💬 Chat RAG com LLaMA + Supabase")

# Histórico de chat
if "history" not in st.session_state:
    st.session_state.history = []

# Entrada do usuário
query = st.chat_input("Digite sua pergunta...")

# Embeddings + Chat model (usando Ollama)
embedding = OllamaEmbeddings(model="llama3:instruct")
llm = ChatOllama(model="llama3:instruct")

# Conexão com o vetor store (Supabase)
vectorstore = SupabaseVectorStore(
    supabase_client=supabase,
    embedding=embedding,
    table_name="documents",
    query_name="match_documents"  # (crie uma RPC no Supabase se necessário)
)

# RAG: Chat com recuperação
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

# Processar pergunta
if query:
    with st.spinner("🔍 Buscando resposta..."):
        result = qa_chain({"query": query})
        resposta = result["result"]

        # Mostrar no chat
        st.session_state.history.append(("Você", query))
        st.session_state.history.append(("Agente", resposta))

# Mostrar histórico
for autor, msg in st.session_state.history:
    with st.chat_message(autor):
        st.markdown(msg)

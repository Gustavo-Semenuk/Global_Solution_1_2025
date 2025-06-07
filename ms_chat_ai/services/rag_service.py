from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.llms import Ollama
from ms_chat_ai.models.supabase_store import get_supabase_vectorstore

# Função que monta a cadeia RAG (Retrieval-Augmented Generation)


def rag_chain():
    retriever = get_supabase_vectorstore().as_retriever()

    prompt = PromptTemplate(
        input_variables=["context"],
        template="""
        Você é um assistente de IA especializado em responder perguntas com base em documentos fornecidos focados em informações de enchentes, alagamentos e chuvas fortes no estado de São Paulo.

Responda sempre em **português**, de forma clara e objetiva. Se não souber a resposta, diga "Desculpe, não encontrei essa informação."

Contexto:

        {context}

        Se a resposta não estiver contida no contexto, diga que não sabe.
        """
    )

    llm = Ollama(model="llama3:instruct")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=False
    )

    return qa_chain

# Função que executa a consulta RAG


def run_rag(query: str) -> dict:
    retriever = get_supabase_vectorstore().as_retriever()
    docs = retriever.get_relevant_documents(query)

    if docs:
        chain = rag_chain()
        result = chain.invoke({"query": query})
        return {"response": result}
    else:
        # fallback: resposta genérica com LLM
        llm = Ollama(model="llama3:instruct")
        response = llm.invoke(query)
        return {"response": response}

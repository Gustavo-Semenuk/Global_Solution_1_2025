import streamlit as st
from streamlit_option_menu import option_menu
import requests
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns


# Estrutura Home
def home():
    st.title("Nossa solução")
    st.write("Transforme seus dados em insights poderosos e revolucione a jornada do cliente\
Nossa plataforma de inteligência de dados foi criada para ajudar empresas como a sua a personalizar a jornada do cliente de forma única.\
Utilizando machine learning, inteligência artificial e modelos avançados de clusterização, extraímos o melhor dos seus dados e de fontes públicas para gerar insights que realmente fazem a diferença.\
")
# Fim da estrura da Home


def formulario():
    st.title("Formulario")


def upload():
    st.title("Upload de Arquivos CSV")

    arquivos = st.file_uploader("Escolha os arquivos", type=[
                                'csv'], accept_multiple_files=True)

    if arquivos:
        st.write(f"{len(arquivos)} arquivo(s) selecionado(s).")

        if st.button("Enviar para o ms-upload"):
            files_to_send = []

            for arquivo in arquivos:
                file_tuple = (
                    "files", (arquivo.name, arquivo.getvalue(), "text/csv"))
                files_to_send.append(file_tuple)

            try:
                response = requests.post(
                    "http://localhost:8000/upload-csv/",  # ou IP público se em nuvem
                    files=files_to_send
                )

                if response.status_code == 200:
                    st.success(response.json()["message"])
                else:
                    st.error(
                        f"❌ Erro: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"❌ Erro de conexão com o microserviço: {e}")


def analise():
    st.title("Análise")
    df = carregar_arquivo_para_dataframe(
        'Challenge_TOTVS_2025_MassaDados_v1/export.csv')

    st.dataframe(df)

    # Resumo do DataFrame
    print("\n📋 Informações gerais:")
    info_geral = df.info()
    info_geral

    # Estatísticas descritivas
    print("\n📊 Estatísticas descritivas:")
    print(df.describe().T)


def cluster():
    st.title('Clusterização')

    # Caminho do arquivo CSV
    caminho_csv = 'Challenge_TOTVS_2025_MassaDados_v1/export.csv'

    # Processar os dados e adicionar a coluna de cluster
    df_clusters = processar_dados_clusterizacao(caminho_csv)

    # Tabela de clientes por cluster
    st.subheader('Tabela de Clientes e seus Clusters')
    tabela = gerar_tabela_clientes_clusters(df_clusters)
    st.dataframe(data=tabela)

    # Seleção das variáveis numéricas para o gráfico
    colunas_numericas = ['VL_TOTAL_CONTRATO',
                         'VLR_CONTRATACOES_12M', 'QTD_CONTRATACOES_12M']
    x_col = st.selectbox(
        'Escolha a variável para o eixo X:', colunas_numericas)
    y_col = st.selectbox('Escolha a variável para o eixo Y:',
                         colunas_numericas, index=1)

    fig = plotar_grafico_clusters(df_clusters, x_col, y_col)
    st.pyplot(fig)


def monitoramento():
    st.title("Monitoramento")


# Sidebar para navegação
st.sidebar.image(
    "D:/Faculdade/Hermes.ai/imagens/logo-backgroud.png", use_container_width=80)

with st.sidebar:
    pagina_selecionada = option_menu(
        "Menu",  # Título do menu
        ["Home", "Formulário", "Upload",
            "Análise", "Clusterização", "Monitoramento"],  # Páginas
        icons=["house", "info", "clipboard",
               "bar-chart", "gear"],  # Ícones (opcional)
        menu_icon="cast",  # Ícone do menu
        default_index=0,  # Índice da página inicial
    )

# Exibir a página selecionada
if pagina_selecionada == "Home":
    home()
elif pagina_selecionada == "Formulário":
    formulario()
elif pagina_selecionada == "Upload":
    upload()
elif pagina_selecionada == "Análise":
    analise()
elif pagina_selecionada == "Clusterização":
    cluster()
elif pagina_selecionada == "Monitoramento":
    monitoramento()

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Estrutura Home
def home():
    col1, col2 = st.columns(2)

    with col1:
        st.header("Vídeo")
        st.write("Transforme seus dados em insights poderosos e revolucione a jornada do cliente\
    Nossa plataforma de inteligência de dados foi criada para ajudar empresas como a sua a personalizar a jornada do cliente de forma única.\
    Utilizando machine learning, inteligência artificial e modelos avançados de clusterização, extraímos o melhor dos seus dados e de fontes públicas para gerar insights que realmente fazem a diferença.\
    ")

    with col2:
        st.header("Nossa solução")
        st.write("Transforme seus dados em insights poderosos e revolucione a jornada do cliente\
    Nossa plataforma de inteligência de dados foi criada para ajudar empresas como a sua a personalizar a jornada do cliente de forma única.\
    Utilizando machine learning, inteligência artificial e modelos avançados de clusterização, extraímos o melhor dos seus dados e de fontes públicas para gerar insights que realmente fazem a diferença.\
    ")
    st.divider()
# Fim da estrura da Home

# Sidebar para navegação
# st.sidebar.image(
 #   "D:/Faculdade/Hermes.ai/imagens/logo-backgroud.png", use_container_width=80)


with st.sidebar:
    pagina_selecionada = option_menu(
        "Menu",  # Título do menu
        ["Home"],  # Páginas
        icons=["house"],  # Ícones (opcional)
        menu_icon="cast",  # Ícone do menu
        default_index=0,  # Índice da página inicial
    )

# Exibir a página selecionada
if pagina_selecionada == "Home":
    home()

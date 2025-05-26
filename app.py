import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

# Estrutura Home


def home():
    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "D:\Faculdade\Global_Solution_1_2025\imagens\logo_rain_of_changes.png")

    with col2:
        st.header("Nossa solução")
        st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
                 "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")


# Sidebar para navegação
st.sidebar.image(
    "D:\Faculdade\Global_Solution_1_2025\imagens\logo_rain_of_changes.png", use_container_width=20)


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

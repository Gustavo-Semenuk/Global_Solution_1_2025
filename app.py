import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import oracledb
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import st_folium
import requests
# import controllers.form_controller as formulario_controler
# import models.form_model as formulario

st.set_page_config(layout="wide")

# Inicializar o geolocalizador
geolocator = Nominatim(user_agent="projeto_streamlit_geopy")

# Função para buscar latitude e longitude pelo CEP


def buscar_lat_lon(cep):
    try:
        location = geolocator.geocode(f"{cep}, Brasil")
        if location:
            return location.latitude, location.longitude
    except:
        return None, None
    return None, None

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


def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            return data
        else:
            print("CEP não encontrado")
            return None
    else:
        print("Erro na API")
        return None

# Página Formulário


# Página Formulário
def formulario():
    st.header("Formulário de Roteiro de Locomoção")

    # Inicializar variáveis na sessão se não existirem
    if 'dados' not in st.session_state:
        st.session_state['dados'] = None

    with st.form(key="cadastro_roteiro"):
        st.subheader("📍 Informações Gerais")
        cidade_moradia = st.text_input("Cidade onde você mora")
        bairro_moradia = st.text_input("Bairro onde você mora*")
        cep_moradia = st.text_input("CEP onde você mora*")
        st.divider()

        # Manhã
        st.subheader("🌅 Roteiro Manhã")
        locomocao_manha = st.radio("Trajeto principal pela manhã:", [
                                   "Trabalho", "Faculdade", "Lazer", "Casa", "Outros"])
        cidade_manha = st.text_input("Cidade de destino (manhã)")
        bairro_manha = st.text_input("Bairro de destino (manhã)")
        cep_manha = st.text_input("CEP de destino (manhã)")
        st.divider()

        # Tarde
        st.subheader("🌞 Roteiro Tarde")
        locomocao_tarde = st.radio("Trajeto principal pela tarde:", [
                                   "Trabalho", "Faculdade", "Lazer", "Casa", "Outros"])
        cidade_tarde = st.text_input("Cidade de destino (tarde)")
        bairro_tarde = st.text_input("Bairro de destino (tarde)")
        cep_tarde = st.text_input("CEP de destino (tarde)")
        st.divider()

        # Noite
        st.subheader("🌙 Roteiro Noite")
        locomocao_noite = st.radio("Trajeto principal pela noite:", [
                                   "Trabalho", "Faculdade", "Lazer", "Casa", "Outros"])
        cidade_noite = st.text_input("Cidade de destino (noite)")
        bairro_noite = st.text_input("Bairro de destino (noite)")
        cep_noite = st.text_input("CEP de destino (noite)")

        # Botão de Enviar
        enviar = st.form_submit_button("Enviar e Mostrar Mapa")

    # Após envio do formulário
    if enviar:
        pontos = []
        for periodo, trajeto, cidade, bairro, cep in zip(
            ["Manhã", "Tarde", "Noite"],
            [locomocao_manha, locomocao_tarde, locomocao_noite],
            [cidade_manha, cidade_tarde, cidade_noite],
            [bairro_manha, bairro_tarde, bairro_noite],
            [cep_manha, cep_tarde, cep_noite]
        ):
            lat, lon = buscar_lat_lon(cep)
            pontos.append({
                "Período": periodo,
                "Trajeto": trajeto,
                "Cidade": cidade,
                "Bairro": bairro,
                "CEP": cep,
                "Latitude": lat,
                "Longitude": lon
            })

        # Salvar dados na sessão
        st.session_state['dados'] = {
            "cidade_moradia": cidade_moradia,
            "bairro_moradia": bairro_moradia,
            "cep_moradia": cep_moradia,
            "pontos": pontos
        }

        st.success("✅ Dados enviados com sucesso! Veja abaixo o mapa e a tabela.")

    # Exibir os dados e o mapa se existirem na sessão
    if st.session_state['dados']:
        dados = st.session_state['dados']
        df = pd.DataFrame(dados["pontos"])
        st.write("📊 Dados coletados:")
        st.dataframe(df)

# Sidebar para navegação
st.sidebar.image(
    "D:\Faculdade\Global_Solution_1_2025\imagens\logo_rain_of_changes.png", use_container_width=20)


with st.sidebar:
    pagina_selecionada = option_menu(
        "Menu",  # Título do menu
        ["Home", "Formulário"],  # Páginas
        icons=["house", "info"],  # Ícones (opcional)
        menu_icon="cast",  # Ícone do menu
        default_index=0,  # Índice da página inicial
    )

# Exibir a página selecionada
if pagina_selecionada == "Home":
    home()
elif pagina_selecionada == "Formulário":
    formulario()

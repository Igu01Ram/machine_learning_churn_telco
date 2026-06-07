import streamlit as st

st.set_page_config(
    page_title="Previsão de Churn",
    page_icon="📊",
    layout="wide"
)

inicio_page = st.Page("pages/0_Inicio.py", title="Início", icon="🏠")
analises_page = st.Page("pages/1_Analises.py", title="Análises", icon="📈")
sobre_page = st.Page("pages/2_Sobre_o_Projeto.py", title="Sobre o Projeto", icon="ℹ️")

pg = st.navigation([inicio_page, analises_page, sobre_page])

pg.run()
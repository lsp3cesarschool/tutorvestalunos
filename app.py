import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="TutorVest: Aluno",
    page_icon="🎓",
    layout="wide",
)

# Caminho do index.html (mesma pasta do app.py)
HTML_PATH = Path(__file__).parent / "index.html"

if not HTML_PATH.exists():
    st.error("Não encontrei o arquivo index.html ao lado do app.py.")
    st.stop()

html = HTML_PATH.read_text(encoding="utf-8")

# Opcional: remover margens do Streamlit para ficar mais "app-like"
st.markdown(
    """
    <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      header {visibility: hidden;}
      .block-container {padding-top: 0.5rem;}
    </style>
    """,
    unsafe_allow_html=True
)

# Ajuste de altura: pode aumentar se sua página for maior
components.html(
    html,
    height=980,
    scrolling=True,
)

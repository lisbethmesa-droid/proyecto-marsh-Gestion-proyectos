import streamlit as st
import streamlit.components.v1 as components
import nbformat
from nbconvert import HTMLExporter

st.set_page_config(page_title="Proyecto Marsh", layout="wide")

NOTEBOOK = "PROYECTO_MARSH_gestion_estrategica.ipynb"

@st.cache_data
def cargar_notebook(ruta):
    nb = nbformat.read(ruta, as_version=4)
    exportador = HTMLExporter()
    exportador.exclude_input = False
    cuerpo, _ = exportador.from_notebook_node(nb)
    return cuerpo

html = cargar_notebook(NOTEBOOK)
components.html(html, height=1000, scrolling=True)

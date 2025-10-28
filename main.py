import streamlit as st
import os
import json
import requests

# URL do arquivo JSON no GitHub
url = "https://github.com/AminRicham/jurisprudencias_streamlit/blob/main/juris.json"

def load_data():
    """Carrega os dados do arquivo JSON"""
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return {"jurisprudencias": []}
        
data = load_data()

st.set_page_config(page_title="Gestão de Jurisprudências")
st.title("Gestão de Jurisprudências")
st.subheader("Lista de Jurisprudências")

if data["jurisprudencias"]:
    for rec in data["jurisprudencias"]:
        st.write(f"**Número:** {rec['numero']}")
        st.write(f"**Tribunal:** {rec['tribunal']}")
        st.write(f"**Data:** {rec['data']}")
        st.write(f"**Tipo:** {rec['tipo']}")
        st.write(f"**Relator:** {rec['relator']}")
        st.write(f"**Assuntos:** {', '.join(rec['assuntos'])}")
        st.write(f"**Palavras-chave:** {', '.join(rec['palavras'])}")
        st.write(f"**Ementa:** {rec['ementa']}")
        st.write(f"**Link:** {rec['link']}")
        st.text("---")  # Separador entre os registros
else:
    st.write("Nenhum registro encontrado.")



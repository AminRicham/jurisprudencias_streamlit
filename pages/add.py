import os
import json
import streamlit as st

# Caminho para o arquivo JSON (caminho relativo a partir da pasta "pages")
DATA_FILE = os.path.join(os.path.dirname(__file__), "../juris.json")

# Funções para carregar, salvar e excluir dados
def load_data():
    """Carrega os dados do arquivo JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"jurisprudencias": []}

def save_data(data):
    """Salva os dados no arquivo JSON"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Carregar dados
data = load_data()

# Exibir os dados
st.title("Gestão de Jurisprudências")
if data["jurisprudencias"]:
    for rec in data["jurisprudencias"]:
        st.write(f"**Número:** {rec['numero']}")
        # Exibir outros dados como você já fez...
else:
    st.write("Nenhum registro encontrado.")

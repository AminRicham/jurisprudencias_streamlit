import streamlit as st
import json
import os

add_page = st.Page("add.py", title="Adicionar jurisprudências")

pg = st.navigation([add_page])
st.set_page_config(page_title="Jurisprudencias")
pg.run()

# Caminho do arquivo JSON
DATA_FILE = "../juris.json"

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

def delete_record(data, id):
    """Exclui um registro pelo ID"""
    data["jurisprudencias"] = [x for x in data["jurisprudencias"] if x["id"] != id]
    save_data(data)

def add_or_update_record(data, rec):
    """Adiciona ou atualiza um registro"""
    idx = next((i for i, x in enumerate(data["jurisprudencias"]) if x["id"] == rec["id"]), None)
    if idx is not None:
        data["jurisprudencias"][idx] = rec  # Atualiza
    else:
        data["jurisprudencias"].insert(0, rec)  # Adiciona no começo
    save_data(data)

# Carregar dados
data = load_data()

# Cabeçalho
st.title("Gestão de Jurisprudências")

# Formulário para adicionar/editar um registro
st.subheader("Adicionar ou Editar Registro")

# Campos do formulário
numero = st.text_input("Número", "")
tribunal = st.text_input("Tribunal", "")
data_registro = st.date_input("Data")
tipo = st.text_input("Tipo", "")
relator = st.text_input("Relator", "")
assuntos = st.text_input("Assuntos (separados por vírgula)", "")
palavras = st.text_input("Palavras (separadas por vírgula)", "")
ementa = st.text_area("Ementa", "")
link = st.text_input("Link", "")

# Lógica para salvar ou atualizar
if st.button("Salvar"):
    rec = {
        "id": numero,  # O id pode ser o número do processo ou um ID único
        "numero": numero,
        "tribunal": tribunal,
        "data": str(data_registro),
        "tipo": tipo,
        "relator": relator,
        "assuntos": [a.strip() for a in assuntos.split(",")],
        "palavras": [p.strip() for p in palavras.split(",")],
        "ementa": ementa,
        "link": link
    }
    add_or_update_record(data, rec)
    st.success("Registro salvo com sucesso!")

# Excluir registros
st.subheader("Excluir Registro")
id_to_delete = st.text_input("ID do registro para excluir", "")
if st.button("Excluir"):
    if id_to_delete:
        delete_record(data, id_to_delete)
        st.success(f"Registro {id_to_delete} excluído com sucesso!")
    else:
        st.error("Por favor, insira um ID para excluir.")

# Exibição de registros
st.subheader("Lista de Jurisprudências")

def show_data():
    # Mostrar dados
    if data["jurisprudencias"]:
        for rec in data["jurisprudencias"]:
            st.write(f"**Número:** {rec['numero']}")
            st.write(f"**Tribunal:** {rec['tribunal']}")
            st.write(f"**Data:** {rec['data']}")
            st.write(f"**Tipo:** {rec['tipo']}")
            st.write(f"**Relator:** {rec['relator']}")
            st.write(f"**Assuntos:** {', '.join(rec['assuntos'])}")
            st.write(f"**Palavras:** {', '.join(rec['palavras'])}")
            st.write(f"**Ementa:** {rec['ementa']}")
            st.write(f"**Link:** {rec['link']}")
            st.text("---")
    else:
        st.write("Nenhum registro encontrado.")







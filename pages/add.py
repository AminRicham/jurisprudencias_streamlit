import streamlit as st

# Verifica se os dados de jurisprudência estão armazenados no session_state
if "jurisprudencias" not in st.session_state:
    st.session_state.jurisprudencias = []  # Inicializa como uma lista vazia se não houver dados

# Configuração da página
st.set_page_config(page_title="Adicionar Jurisprudência")

# Cabeçalho da página de adição
st.title("Adicionar Nova Jurisprudência")

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

    # Adiciona o novo registro à lista de jurisprudências no session_state
    st.session_state.jurisprudencias.insert(0, rec)  # Adiciona no começo
    st.success("Registro salvo com sucesso!")

# Link para voltar para a página principal
st.sidebar.markdown("[Voltar para a lista de jurisprudências](main.py)")

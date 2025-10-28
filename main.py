import streamlit as st

# Verifica se os dados de jurisprudência estão armazenados no session_state
if "jurisprudencias" not in st.session_state:
    st.session_state.jurisprudencias = []  # Inicializa como uma lista vazia se não houver dados

# Configuração da página
st.set_page_config(page_title="Gestão de Jurisprudências")

# Cabeçalho da página principal
st.title("Gestão de Jurisprudências")

# Exibir todas as jurisprudências
st.subheader("Lista de Jurisprudências")

if st.session_state.jurisprudencias:
    for rec in st.session_state.jurisprudencias:
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

# Adicionar link para a página de adição
st.sidebar.title("Navegação")
st.sidebar.markdown("[Adicionar Jurisprudência](add.py)")  # Link para a página de adição

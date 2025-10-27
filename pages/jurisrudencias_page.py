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

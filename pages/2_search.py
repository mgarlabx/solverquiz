import streamlit as st
import functions.enade.enade as enade

if 'curso' not in st.session_state:
    st.switch_page("pages/1_config.py")

openai_api_key = st.secrets['OPENAI_API_KEY']

curso = st.session_state['curso']
assunto = st.session_state['assunto']

st.header("Buscar sites na web")
st.write(f"Curso: {curso}")
st.write(f"Assunto: {assunto}")

if st.button("Buscar"):
    with st.spinner("Buscando..."):
        resultados = enade.search(curso, assunto, openai_api_key)
        if resultados:
            st.success(f"Encontrados {len(resultados)} sites.")
            for site in resultados:
                st.markdown(f"- [{site['title']}]({site['url']})")
        else:
            st.warning("Nenhum site encontrado para o assunto selecionado.")

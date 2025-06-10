import streamlit as st
import json

with open("portarias.json", "r") as file:
    portarias = file.read()

portarias = json.loads(portarias)
cursos = [curso["curso"] for curso in portarias]

st.header("Configurar")

curso = st.selectbox(
    "Selecione o curso",
    options=cursos
)

portaria = next(c for c in portarias if c["curso"] == curso)
caracteristicas = portaria["caracteristicas"]
competencias = portaria["competencias"]
assuntos = portaria["assuntos"]
url = portaria["url"]

assunto = st.selectbox(
    "Selecione o assunto",
    options=assuntos
)

st.link_button("Clique aqui para acessar o Edital", url)

st.session_state['curso'] = curso
st.session_state['assunto'] = assunto
st.session_state['caracteristicas'] = caracteristicas
st.session_state['competencias'] = competencias
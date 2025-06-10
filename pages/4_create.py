import streamlit as st
import functions.enade.enade as enade
import functions.db.db as db

if 'item_key' not in st.session_state:
    st.switch_page("pages/3_list.py")

def write_question(question):
    st.write(texto_base)
    st.write(referencia)
    st.write(question["enunciado"])
    st.write("A. " + question["alternativa_1"])
    st.write("B. " + question["alternativa_2"])
    st.write("C. " + question["alternativa_3"])
    st.write("D. " + question["alternativa_4"])
    st.write("E. " + question["alternativa_5"])
    st.divider()
    st.write(f"Resposta correta: {question['correta']}")
    st.divider()
    st.write(question["justificativa_1"])
    st.write(question["justificativa_2"])
    st.write(question["justificativa_3"])
    st.write(question["justificativa_4"])
    st.write(question["justificativa_5"])

openai_api_key = st.secrets['OPENAI_API_KEY']

curso = st.session_state['curso']
assunto = st.session_state['assunto']
caracteristicas = st.session_state['caracteristicas']
competencias = st.session_state['competencias']
texto_base = st.session_state['item_abstract']
referencia = st.session_state['item_reference']

st.header("Elaborar questão de Enade")
st.write(f"Curso: {curso}")
st.write(f"Assunto: {assunto}")
st.write(st.session_state['item_url'])

c1, c2 = st.columns([2,5])

# Tipo de questão
tipo = c1.radio(
    "Tipo de questão:",
    options=["Resposta única", "Resposta múltipla", "Asserção/Razão"],
)
ttipo = 0
if tipo == "Resposta múltipla": ttipo = 1
elif tipo == "Asserção/Razão": ttipo = 2
st.session_state['tipo_questao'] = ttipo

# Grau de dificuldade da questão
nivel = c2.radio(
    "Grau de dificuldade:",
    options=["Fácil", "Média", "Difícil"],
)
nnivel = 0
if nivel == "Média": nnivel = 1
elif nivel == "Difícil": nnivel = 2
st.session_state['nivel_questao'] = nnivel

if st.button("Criar questão"):
    with st.spinner("Criando questão..."):
        question = enade.create(curso, assunto, caracteristicas, competencias, texto_base, ttipo, nnivel, openai_api_key)
        st.session_state['question'] = question
        write_question(question)
        st.button("Salvar questão", on_click=db.insert_item)
    
 
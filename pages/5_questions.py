import streamlit as st
import json
from io import BytesIO
import functions.db.db as db


    
# Calcula a altura do campo de texto baseado no tamanho do texto
def get_height(text):
    line_breaks = text.count('\n')
    if line_breaks < 2: line_breaks = 2
    return int(len(text) / 5) + line_breaks * 20 + 50

# Carrega as questões do banco de dados
questions = db.get_items()

# Cabeçalho da página
st.header("Consulta de questões")

# Percorre as questões e exibe os detalhes
for question in questions:

    # Define o tipo da questão
    tipo = "Resposta única"
    if question['tipo_questao'] == "1":
        tipo = "Resposta múltipla"
    elif question['tipo_questao'] == "2":
        tipo = "Asserção/Razão"

    # Define o nível (grau de dificuldade)
    nivel = "Fácil"
    if question['nivel_questao'] == "1":
        nivel = "Média"
    elif question['nivel_questao'] == "2":
        nivel = "Difícil"

    

    # Formata a data de criação DD/MM/AAAA HH:MM
    data = question['data_insert']
    hora = data[11:16]
    data = data[:10]
    data = data.split("-")
    data = f"{data[2]}/{data[1]}/{data[0]} {hora}"
    
    # Exibe os detalhes da questão
    st.subheader(f"Questão ID {question['id']}")
    st.write(f"**Data de criação:** {data}")
    c1, c2 = st.columns(2)
    c1.write(f"**Tipo:** {tipo}")
    c2.write(f"**Nível:** {nivel}")
    st.write(f"**Curso:** {question['curso']}")
    st.write(f"**Assunto:** {question['assunto']}")

    # Exibe o conteúdo da questão para edição
    with st.expander("Questão", expanded=False):

        tx_texto_base = st.text_area("Texto-base", question['texto_base'], key=f"tx_texto_base_{question['id']}", height=get_height(question['texto_base']))
        tx_referencia = st.text_area("Referência", question['referencia'], key=f"tx_referencia_{question['id']}", height=get_height(question['referencia']))
        tx_enunciado = st.text_area("Enunciado", question['enunciado'], key=f"tx_enunciado_{question['id']}", height=get_height(question['enunciado']))
        tx_alternativa_1 = st.text_input("Alternativa A", question['alternativa_1'], key=f"tx_alternativa_1_{question['id']}")
        tx_alternativa_2 = st.text_input("Alternativa B", question['alternativa_2'], key=f"tx_alternativa_2_{question['id']}")
        tx_alternativa_3 = st.text_input("Alternativa C", question['alternativa_3'], key=f"tx_alternativa_3_{question['id']}")
        tx_alternativa_4 = st.text_input("Alternativa D", question['alternativa_4'], key=f"tx_alternativa_4_{question['id']}")
        tx_alternativa_5 = st.text_input("Alternativa E", question['alternativa_5'], key=f"tx_alternativa_5_{question['id']}")
        tx_correta = st.text_input("Alternativa correta", question['correta'], key=f"tx_correta_{question['id']}")
        tx_justificativa_1 = st.text_area("Justificativa A", question['justificativa_1'], key=f"tx_justificativa_1_{question['id']}", height=get_height(question['justificativa_1']))
        tx_justificativa_2 = st.text_area("Justificativa B", question['justificativa_2'], key=f"tx_justificativa_2_{question['id']}", height=get_height(question['justificativa_2']))
        tx_justificativa_3 = st.text_area("Justificativa C", question['justificativa_3'], key=f"tx_justificativa_3_{question['id']}", height=get_height(question['justificativa_3']))   
        tx_justificativa_4 = st.text_area("Justificativa D", question['justificativa_4'], key=f"tx_justificativa_4_{question['id']}", height=get_height(question['justificativa_4']))
        tx_justificativa_5 = st.text_area("Justificativa E", question['justificativa_5'], key=f"tx_justificativa_5_{question['id']}", height=get_height(question['justificativa_5']))

        if st.button("Salvar", key=f"confirm_salva_{question['id']}"):
            new_question = {
                'id': question['id'],
                'texto_base': tx_texto_base,
                'referencia': tx_referencia,
                'enunciado': tx_enunciado,
                'alternativa_1': tx_alternativa_1,
                'alternativa_2': tx_alternativa_2,
                'alternativa_3': tx_alternativa_3,
                'alternativa_4': tx_alternativa_4,
                'alternativa_5': tx_alternativa_5,
                'correta': tx_correta,
                'justificativa_1': tx_justificativa_1,
                'justificativa_2': tx_justificativa_2,
                'justificativa_3': tx_justificativa_3,  
                'justificativa_4': tx_justificativa_4,
                'justificativa_5': tx_justificativa_5
            }
            db.save_item(new_question)
            st.success("Questão salva com sucesso!")

    # Colunas para os botões de download e exclusão   
    c1, c2 = st.columns([1,4])
   
    # Botão para baixar a questão
    question_json = json.dumps(dict(question), ensure_ascii=False, indent=2)
    buffer = BytesIO(question_json.encode('utf-8'))
    c1.download_button(
        label="Baixar JSON",
        data=buffer,
        file_name=f"solverquiz_questao_{question['id']}.json",
        mime="application/json",
        key=f"download_btn_{question['id']}"
    )

    # Botão para excluir a questão
    if f"confirmed_{question['id']}" not in st.session_state:
        st.session_state[f"confirmed_{question['id']}"] = False
    if c2.button("Excluir questão", key=f"delete_{question['id']}"):
        st.session_state[f"confirmed_{question['id']}"] = True
    if st.session_state[f"confirmed_{question['id']}"]:
        st.warning(f"Você tem certeza que deseja excluir a questão ID {question['id']}?")
        if st.button("Confirmar exclusão", key=f"delete_confirm_{question['id']}"):
            st.session_state[f"confirmed_{question['id']}"] = False
            db.delete_item(question['id'])
            st.rerun()

    # Separador entre as questões
    st.divider()
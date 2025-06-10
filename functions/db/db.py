import streamlit as st

# Recupera os itens do banco de dados
def get_items():
    conn = st.connection('questoes_db', type='sql')
    with conn.session as s:
        sql = "SELECT * FROM tb_questoes;"
        result = s.execute(sql)
        items = result.fetchall()
    return items

# Insere um novo item no banco de dados
def insert_item():

    zotero_collection_key = st.secrets['ZOTERO_COLLECTION_KEY']
    zotero_item_key       = st.session_state['item_key'] 
    curso                 = st.session_state['curso']
    assunto               = st.session_state['assunto']
    texto_base            = st.session_state['item_abstract']
    referencia            = st.session_state['item_reference']
    tipo_questao          = st.session_state['tipo_questao']
    nivel_questao         = st.session_state['nivel_questao']
    enunciado             = st.session_state['question']['enunciado']
    alternativa_1         = st.session_state['question']['alternativa_1']
    alternativa_2         = st.session_state['question']['alternativa_2']
    alternativa_3         = st.session_state['question']['alternativa_3']
    alternativa_4         = st.session_state['question']['alternativa_4']
    alternativa_5         = st.session_state['question']['alternativa_5']
    correta               = st.session_state['question']['correta']
    justificativa_1       = st.session_state['question']['justificativa_1']
    justificativa_2       = st.session_state['question']['justificativa_2']
    justificativa_3       = st.session_state['question']['justificativa_3']
    justificativa_4       = st.session_state['question']['justificativa_4']
    justificativa_5       = st.session_state['question']['justificativa_5']

    sql = f"""INSERT INTO tb_questoes 
        (
            zotero_collection_key,
            zotero_item_key,
            curso,
            assunto,
            texto_base,
            referencia, 
            tipo_questao,
            nivel_questao,
            enunciado,
            alternativa_1,
            alternativa_2,
            alternativa_3,
            alternativa_4,
            alternativa_5,
            correta,
            justificativa_1,
            justificativa_2,
            justificativa_3,
            justificativa_4,
            justificativa_5
        )
        VALUES
        (
            '{zotero_collection_key}',
            '{zotero_item_key}',
            '{curso}',
            '{assunto}',
            '{texto_base}',
            '{referencia}',
            '{tipo_questao}',
            '{nivel_questao}',
            '{enunciado}',
            '{alternativa_1}',
            '{alternativa_2}',
            '{alternativa_3}',
            '{alternativa_4}',
            '{alternativa_5}',
            '{correta}',
            '{justificativa_1}',
            '{justificativa_2}',
            '{justificativa_3}',
            '{justificativa_4}',
            '{justificativa_5}'
        );"""

    conn = st.connection('questoes_db', type='sql')
    with conn.session as s:
        s.execute(sql)
        s.commit()

# Exclui um item do banco de dados
def delete_item(item_id):
    sql = f"DELETE FROM tb_questoes WHERE id = {item_id};"
    conn = st.connection('questoes_db', type='sql')
    with conn.session as s:
        s.execute(sql)
        s.commit()

# Atualiza um item existente no banco de dados
def save_item(item):
    sql = f"""UPDATE tb_questoes SET
        texto_base = '{item['texto_base']}',
        referencia = '{item['referencia']}',
        enunciado = '{item['enunciado']}',
        alternativa_1 = '{item['alternativa_1']}',
        alternativa_2 = '{item['alternativa_2']}',
        alternativa_3 = '{item['alternativa_3']}',
        alternativa_4 = '{item['alternativa_4']}',
        alternativa_5 = '{item['alternativa_5']}',
        correta = '{item['correta']}',
        justificativa_1 = '{item['justificativa_1']}',
        justificativa_2 = '{item['justificativa_2']}',
        justificativa_3 = '{item['justificativa_3']}',
        justificativa_4 = '{item['justificativa_4']}',
        justificativa_5 = '{item['justificativa_5']}'
        WHERE id = {item['id']};"""

    conn = st.connection('questoes_db', type='sql')
    with conn.session as s:
        s.execute(sql)
        s.commit()
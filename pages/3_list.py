import streamlit as st
import functions.zotero.zotero as zotero

if 'curso' not in st.session_state:
    st.switch_page("pages/1_config.py")

zotero_user_id = st.secrets['ZOTERO_USER_ID']
zotero_api_key = st.secrets['ZOTERO_API_KEY']
ZOTERO_COLLECTION_KEY = st.secrets['ZOTERO_COLLECTION_KEY']

curso = st.session_state['curso']
assunto = st.session_state['assunto']

st.header("Listar sites salvos no Zotero")
st.write(f"Curso: {curso}")
st.write(f"Assunto: {assunto}")

with st.spinner("Buscando..."):
    zotero_items = zotero.get_items(ZOTERO_COLLECTION_KEY, zotero_user_id, zotero_api_key)
    for item in zotero_items:
        st.markdown(f"[{item['title']}]({item['url']})")
        st.write(f"{item['abstract']}")
        st.caption(f"Chave: {item['key']}")
        c1, c2 = st.columns([1,5])
        if c1.button("Selecionar", key='s' + item['key']):
            with st.spinner("Carregando item selecionado..."):
                selected_item = zotero.get_item(item['key'], zotero_user_id, zotero_api_key)
                st.session_state['item_reference'] = selected_item['reference']
                st.session_state['item_key'] = item['key']
                st.session_state['item_title'] = item['title']
                st.session_state['item_url'] = item['url']
                st.session_state['item_abstract'] = item['abstract']
                st.success(f"Item '{item['title']}' selecionado com sucesso!")
                st.switch_page("pages/4_create.py")
        if c2.button("Excluir", key='e' + item['key']):
            with st.spinner("Excluindo item..."):
                deleted_item = zotero.delete_item(item['key'], item['version'], zotero_user_id, zotero_api_key)
                st.rerun()
                

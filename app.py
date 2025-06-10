import streamlit as st

pages = {"SolverQuiz": [
    st.Page("pages/1_config.py", title="1. Selecionar"),
    st.Page("pages/2_search.py", title="2. Buscar"),
    st.Page("pages/3_list.py", title="3. Listar"),
    st.Page("pages/4_create.py", title="4. Elaborar"),
    st.Page("pages/5_questions.py", title="5. Consultar"),
]}
pg = st.navigation(pages)
pg.run()




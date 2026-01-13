import streamlit as st

pg = st.navigation(
    [
        st.Page("page_1.py"),
        st.Page("page_2.py"),
    ]
)

for key in st.session_state:
    st.session_state[key] = st.session_state[key]


pg.run()

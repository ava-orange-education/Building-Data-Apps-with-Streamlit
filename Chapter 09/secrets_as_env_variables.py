import streamlit as st

with st.echo():
    import os

    import streamlit as st

    st.write("Username:", os.getenv("username"))
    st.write("Password:", os.getenv("password"))

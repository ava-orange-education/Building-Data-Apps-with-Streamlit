import streamlit as st

with st.echo():
    from time import sleep

    if st.button("Login"):
        st.toast("Logging in...", icon=":material/lock:")
        sleep(2)
        st.toast("Logged in successfully!", icon=":material/lock_open:")

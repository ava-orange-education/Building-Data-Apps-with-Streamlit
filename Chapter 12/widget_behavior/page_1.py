import streamlit as st

st.title("Page 1")
st.text_input("Enter your name", key="name")
st.write(f"Hello, {st.session_state.name}!")

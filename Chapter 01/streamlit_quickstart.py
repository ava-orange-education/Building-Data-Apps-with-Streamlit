import streamlit as st

if name := st.text_input("Enter your name:"):
    st.write(f"Hello, {name}!")

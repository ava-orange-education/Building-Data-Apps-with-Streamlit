import streamlit as st

with st.echo():
    if picture := st.camera_input("Take a picture"):
        st.image(picture)

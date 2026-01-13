import streamlit as st

with st.echo():
    placeholder = st.empty()

    placeholder.text("Default widget")

    if st.button("Replace widget"):
        placeholder.text("Widget replaced")

    if st.button("Clear widget"):
        placeholder.empty()

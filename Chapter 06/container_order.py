import streamlit as st

with st.echo():
    container = st.container()
    container.write("Line 1: This is inside the container")
    st.write("Line 2: This is outside the container")
    container.write("Line 3: This is inside too")

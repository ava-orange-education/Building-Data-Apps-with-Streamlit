import streamlit as st

with st.echo():
    image_url = "https://static.streamlit.io/examples/cat.jpg"

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Without container")
        st.image(image_url, width=250)

    with col2:
        with st.container(height=300):
            st.subheader("With container")
            st.image(image_url, width=250)

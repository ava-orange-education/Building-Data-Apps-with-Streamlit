import streamlit as st

st.subheader("Creating widget using `column` object")

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor."

with st.echo():
    col1, col2 = st.columns(2)

    col1.write("Column 1")
    col1.write(text)

    col2.write("Column 2")
    col2.write(text)

st.subheader("Creating widgets using `column` as context manager")

with st.echo():
    col1, col2 = st.columns(2)

    with col1:
        st.write("Column 1")
        st.write(text)

    with col2:
        st.write("Column 2")
        st.write(text)

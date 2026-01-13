





import streamlit as st

st.title("This is a title")

st.header("This is a header", divider=True)



st.subheader("This is a subheader", divider=True)


st.text("This is a text")

st.markdown("__This__ is a _markdown_")


st.latex("This\:is\:\LaTeX")

st.caption("This is a caption")



st.code("print('This is a code block')", line_numbers=True)


with st.echo():
    st.write("This is an echo")





with st.chat_message(name="user"):
    st.write("This is a user chat message")



with st.chat_message(name="assistant"):
    st.write("This is a bot chat message")






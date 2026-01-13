import streamlit as st

st.write("Initial `name`: ", st.session_state.get("name"))

if "name" not in st.session_state:
    st.session_state.name = "Awesome Reader"

st.write("`name` after adding key:", st.session_state.name)

st.session_state.name = "Another Awesome Reader"
st.write("`name` after updating before widget: ", st.session_state.name)

st.text_input("Enter your name", key="name", value="John Doe")
st.write("`name` after widget: ", st.session_state.name)

st.session_state.name = "Still Another Awesome Reader"
st.write("`name` after updating after widget: ", st.session_state.name)

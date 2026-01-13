import streamlit as st

st.session_state.number_input = st.session_state.get("number_input")

st.number_input("Enter a number", key="number_input")
st.write(st.session_state.number_input)

for key in st.session_state:
    st.session_state["key"] = st.session_state["key"]
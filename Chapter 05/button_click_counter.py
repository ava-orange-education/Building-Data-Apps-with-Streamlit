import streamlit as st

st.write("Starting script")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Click me!"):
    st.session_state["count"] += 1
    st.write(f"Button was clicked {st.session_state.count} times")

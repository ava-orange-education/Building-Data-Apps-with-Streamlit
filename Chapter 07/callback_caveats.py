import streamlit as st

st.header("Callback Caveats")


def write_something():
    st.write("Hello, Awesome Reader!")
    st.session_state.clicked = True


st.button("Click to start", on_click=write_something)

if st.session_state.get("clicked"):
    if st.button("Click again"):
        st.write("Second click")

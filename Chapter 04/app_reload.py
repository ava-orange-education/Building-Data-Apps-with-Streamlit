import streamlit as st

st.write("Starting script")

st.write("Button1 state before:", st.session_state.get("button1"))
st.write("Button2 state before:", st.session_state.get("button2"))

if st.button("Click me!", key="button1"):
    st.write("Button1 was clicked")
    st.write("Button1 state after:", st.session_state.button1)

    if st.button("Click me too!", key="button2"):
        st.write("Button2 was clicked")
        st.write("Button2 state after:", st.session_state.button2)

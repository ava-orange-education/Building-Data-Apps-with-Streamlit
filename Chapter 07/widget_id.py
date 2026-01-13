import streamlit as st

st.button("Click here")

st.write(st.runtime.scriptrunner.get_script_run_ctx().session_state)

st.button("Click here", key="my_button")

st.write(st.runtime.scriptrunner.get_script_run_ctx().session_state)

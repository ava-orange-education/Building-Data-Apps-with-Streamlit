import streamlit as st

with st.echo():
    st.success("This is a success message", icon=":material/check_circle:")
    st.info("This is an info message", icon=":material/info:")
    st.warning("This is a warning message", icon=":material/warning:")
    st.error("This is an error message", icon=":material/error:")
    st.exception(RuntimeError("This is an exception"))

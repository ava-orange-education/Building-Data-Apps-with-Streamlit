import streamlit as st

st.set_option("client.showErrorDetails", True)
if st.button("Hide error details"):
    st.set_option("client.showErrorDetails", False)
    st.write("Error details are now hidden.")
else:
    st.write("Error details are now visible.")
raise RuntimeError("This is an error message.")

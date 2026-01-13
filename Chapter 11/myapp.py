import streamlit as st

st.set_option("client.showErrorDetails", False)
st.write(st.get_option("client.showErrorDetails"))

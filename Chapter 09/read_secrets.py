import streamlit as st

st.header("Root credentials")
st.write("Root username: ", st.secrets["username"])
st.write("Root password: ", st.secrets["password"])

st.header("Database 1 credentials")
st.write("Database 1 username:", st.secrets["database_1"]["username"])
st.write("Database 1 password:", st.secrets["database_1"]["password"])

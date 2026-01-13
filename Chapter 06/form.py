import streamlit as st

with st.echo():
    with st.form("my_form"):
        fname = st.text_input("First Name")
        lname = st.text_input("Last Name")
        submit = st.form_submit_button("Submit")
    if submit:
        st.write(f"Welcome, {fname} {lname}")

import streamlit as st

with st.echo():
    tab1, tab2 = st.tabs(["Tab1", "Tab2"])

    with tab1:
        tab1_text = st.text_input("Enter some text")
        number = st.number_input("Enter a number")

    with tab2:
        tab2_text = st.text_input("Enter some different text")
        number = st.number_input("Enter a different number")

    st.write(f"{tab1_text=}")
    st.write(f"{tab2_text=}")
    st.write(f"{number=}")

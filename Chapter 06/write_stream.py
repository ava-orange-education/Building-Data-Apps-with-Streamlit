from time import sleep

import streamlit as st


def number_stream():
    for i in range(10):
        yield i
        sleep(0.5)


def text_stream():
    for i in range(10):
        yield str(i) + " "
        sleep(0.5)


st.write_stream(number_stream)
st.write_stream(text_stream)

import numpy as np
import pandas as pd
import streamlit as st

st.title("Quick Widget Recap")

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

st.header("Inputs", divider=True)

name = st.text_input(
    "Enter your name",
    placeholder="Type here...",
)

number = st.number_input(
    "Enter a number",
    min_value=20,
    max_value=60,
)

animal = st.selectbox(
    "Pick an animal",
    options=["🐶 Dog", "😺 Cat", "🐰 Rabbit"],
)

if st.button("Show chart"):
    st.session_state.button_clicked = True

st.header("Outputs", divider=True)

st.write(f"Hello, _{name}_ :wave:")
st.write(f"Showing __{number}__ points")

if st.session_state.button_clicked:
    chart_data = pd.DataFrame(
        np.random.randn(number, 4),
        columns=["a", "b", "c", "d"],
    )

    st.scatter_chart(chart_data)




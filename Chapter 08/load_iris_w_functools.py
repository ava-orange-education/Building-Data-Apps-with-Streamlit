import streamlit as st

st.title("With `functools.cache`")

with st.echo():
    from functools import cache
    from time import perf_counter

    import pandas as pd
    import streamlit as st

    url = "https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/iris.csv"

    start = perf_counter()

    @cache
    def load_data(url):
        return pd.read_csv(url)

    df = load_data(url)
    st.write(f"Time taken: {(perf_counter() - start):.3f}s")

    st.button("Rerun")

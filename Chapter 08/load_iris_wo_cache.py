import streamlit as st

st.title("Without cache")

with st.echo():
    from time import perf_counter

    import pandas as pd
    import streamlit as st

    url = "https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/iris.csv"

    start = perf_counter()
    df = pd.read_csv(url)
    st.write(f"Time taken: {(perf_counter() - start):.3f}s")

    st.button("Rerun")

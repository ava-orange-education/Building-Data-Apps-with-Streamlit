import streamlit as st

with st.echo():
    from random import randint

    data = {"value": [randint(0, 10) for _ in range(10)]}

    tab1, tab2 = st.tabs(["Chart", "Data"])

    with tab1:
        st.write("Here's a chart")
        st.line_chart(data)

    with tab2:
        st.write("Here's the data")
        st.dataframe(data)

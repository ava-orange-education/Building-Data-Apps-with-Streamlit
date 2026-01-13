import streamlit as st

with st.echo():
    import numpy as np
    import pandas as pd
    import streamlit as st

    df = pd.DataFrame({"A": np.random.randn(100), "B": np.random.rand(100)})

    df.to_csv("data.csv", index=False)

    st.download_button(
        "Download CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="dataframe.csv",
        mime="text/csv",
    )

    st.download_button(
        "Download text",
        data="Hello, world!",
    )

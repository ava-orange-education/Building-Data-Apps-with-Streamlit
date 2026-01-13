import pandas as pd
import streamlit as st

df = pd.DataFrame(
    {
        "Ch. #": [1, 2, 3, 4, 5],
        "Title": [
            "Introduction to Streamlit",
            "Setting up the Development Environment",
            "Creating and Deploying Your First Streamlit App",
            "Exploring Streamit's Flow and Architecture",
            "Persisting Data and State Using Session State",
        ],
        "Rating": [3, 3, 3, 3, 3],
    },
)

st.write("This is a static table")
st.table(df)

st.write("This is an interactive table")
st.dataframe(df)

st.write("This is an editable table")
edited_df = st.data_editor(df)

st.write(
    f"Highest rated chapter: __{edited_df['Title'][edited_df['Rating'].idxmax()]}__"
)

st.metric(
    "__Average Rating__",
    edited_df["Rating"].mean(),
    edited_df["Rating"].mean() - df["Rating"].mean(),
)

import seaborn as sns
import streamlit as st

st.title("Iris Analysis App")

iris_df = sns.load_dataset("iris")

st.header("Dataset")
st.write(iris_df)

st.header("Dataset description")
st.write(iris_df.describe())

x = st.selectbox(
    "Enter x-axis column: ",
    options=iris_df.columns,
)
y = st.selectbox(
    "Enter y-axis column: ",
    options=iris_df.columns,
)

st.scatter_chart(x=x, y=y, data=iris_df, color="species")

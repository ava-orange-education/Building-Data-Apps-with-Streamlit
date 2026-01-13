import streamlit as st

with st.sidebar:
    st.subheader("Widgets")
    st.button("Sample Primary Button", type="primary")
    st.button("Sample Secondary Button")
    st.checkbox("Sample Checkbox")
    st.radio("Sample Radio", ["Option 1", "Option 2", "Option 3"])
    st.subheader("Dataframe")
    st.dataframe({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})

st.title("Streamlit Theme Demo")
st.write("This is a simple app to demonstrate different theme options in Streamlit.")

st.header("Sample Content")
st.write("You can add any content here to see how it looks with different themes.")

st.subheader("Charts")
st.bar_chart([5, 4, 3, 2, 1])

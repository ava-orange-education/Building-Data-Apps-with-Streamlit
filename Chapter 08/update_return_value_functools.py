import streamlit as st

st.title("Using `functools.cache`")

with st.echo():
    from functools import cache

    import streamlit as st

    @cache
    def create_list():
        return [1, 2, 3]

    my_list = create_list()
    st.write("Before updating:", my_list)

    my_list[1] = 4

    st.write("After updating:", create_list())

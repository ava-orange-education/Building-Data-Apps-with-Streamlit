import streamlit as st

st.title("Main Page")


def page_one():
    st.title("Page One")


def page_two():
    st.title("Page Two")


def page_three():
    st.title("Page Three")


pg = st.navigation(
    [
        st.Page(page_one),
        st.Page(page_two),
        st.Page(
            page_three,
            title="Page Three",
            icon=":material/timer_3:",
            url_path="third_page",
        ),
    ]
)

pg.run()

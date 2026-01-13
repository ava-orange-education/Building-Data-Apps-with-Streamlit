import streamlit as st

pg = st.navigation(
    [
        st.Page("page_one.py"),
        st.Page("some_folder/page_two.py"),
        st.Page(
            "page_three.py",
            title="Page Three",
            icon=":material/timer_3:",
            url_path="third_page",
        ),
    ]
)

pg.run()

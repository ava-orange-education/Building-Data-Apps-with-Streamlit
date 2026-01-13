import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get help": "mailto:awesome.reader@example.com",  # Send an email to this address
        "Report a Bug": "https://github.com/AwesomeReader/AwesomeApp/issues/new",  # Open a GitHub issue
        "About": ":fire: Awesome App! Developer: [Awesome Reader](mailto:awesomereader@example.com)",  # Custom About section
    },
)

st.title("Page One")

st.caption([i for i in range(100)])

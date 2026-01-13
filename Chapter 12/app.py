import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()


def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.switch_page(about_page)


def profile():
    st.title("Profile")


def home():
    st.title("Home")


def about():
    st.title("About")


def contact():
    st.title("Contact details")


home_page = st.Page(home, title="Home", icon=":material/home:")
login_page = st.Page(login, title="Log in", icon=":material/login:")
profile_page = st.Page(profile, title="Profile", icon=":material/account_circle:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
about_page = st.Page(about, title="About", icon=":material/info:")
contact_page = st.Page(contact, title="Contact", icon=":material/contact_support:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "": [home_page],
            "User": [profile_page, logout_page],
            "Info": [about_page, contact_page],
        },
        position="hidden",
    )

else:
    pg = st.navigation(
        {
            "User": [login_page],
            "Info": [about_page, contact_page],
        },
        position="hidden",
    )

with st.sidebar:
    st.page_link(
        home_page,
        icon=":material/home:",
        disabled=not st.session_state.logged_in,
    )
    st.write("User")
    st.page_link(
        login_page,
        icon=":material/login:",
        disabled=st.session_state.logged_in,
    )
    st.page_link(
        profile_page,
        icon=":material/account_circle:",
        disabled=not st.session_state.logged_in,
    )
    st.page_link(
        logout_page,
        icon=":material/logout:",
        disabled=not st.session_state.logged_in,
    )
    st.write("Info")
    st.page_link(about_page, icon=":material/info:")
    st.page_link(contact_page, icon=":material/contact_support:")
    st.page_link(
        "https://www.streamlit.io",
        label="Streamlit",
        icon=":material/open_in_new:",
    )

pg.run()

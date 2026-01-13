import json

import streamlit as st

with open("users.json", "r") as file:
    users = json.load(file)

st.title("A Well-Tested App!")

if not st.session_state.get("role"):
    with st.form("login_form"):
        st.session_state.username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.form_submit_button(
            "Login",
            use_container_width=True,
            type="primary",
            icon=":material/login:",
        ):
            if (
                st.session_state.username in users
                and users[st.session_state.username]["password"] == password
            ):
                st.session_state.role = users[st.session_state.username]["role"]
                st.rerun()
            else:
                st.error(
                    "Login failed. Incorrect username/password.",
                    icon=":material/lock:",
                )
else:
    with st.sidebar:
        st.success(
            f"Welcome **{st.session_state.get('username')}** ({st.session_state.get('role')}) :wave:"
        )

        if st.button("Logout", icon=":material/logout:", use_container_width=True):
            st.navigation([st.Page("login.py")])
            st.session_state.clear()
            st.rerun()

    bells_and_whistles_page = st.Page(
        "bells_and_whistles.py",
        title="Bells and Whistles",
        icon=":material/engineering:",
    )

    if st.session_state.role == "admin":
        pg = st.navigation(
            [
                st.Page(
                    "manage_users.py",
                    title="Manage Users",
                    icon=":material/people:",
                ),
                bells_and_whistles_page,
            ]
        )
    else:
        pg = st.navigation([bells_and_whistles_page])

    pg.run()

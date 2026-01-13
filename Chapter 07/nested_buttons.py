import streamlit as st

with st.echo():
    import streamlit as st

    st.write("Button1 clicked:", st.session_state.get("button_1"))
    st.write("Button2 clicked:", st.session_state.get("button_2"))

    def update_status(button, state):
        st.session_state[button] = state

    st.button("Click me!", on_click=update_status, args=("button_1", True))

    if st.session_state.get("button_1"):
        st.write("Button1 was clicked")

        st.button(
            "Click me too!",
            on_click=update_status,
            args=("button_2", True),
        )

        if st.session_state.get("button_2"):
            st.write("Button2 was clicked")

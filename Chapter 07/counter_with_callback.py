import streamlit as st

with st.echo():
    import streamlit as st

    st.write("Starting script")

    if "count" not in st.session_state:
        st.session_state.count = 0

    def increment_count():
        st.session_state.count += 1

    st.button("Click me!", on_click=increment_count)
    st.write(f"Button was clicked {st.session_state.count} times")

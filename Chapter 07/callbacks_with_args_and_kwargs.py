import streamlit as st

with st.echo():
    import streamlit as st

    if "count" not in st.session_state:
        st.session_state.count = 0

    def change_count(kind, change_by):
        if kind == "increase":
            st.session_state.count += change_by
        elif kind == "decrease":
            st.session_state.count -= change_by

    st.button(
        "Increase by 5",
        on_click=change_count,
        args=("increase", 5),
    )
    st.button(
        "Decrease by 2",
        on_click=change_count,
        kwargs=dict(kind="decrease", change_by=2),
    )

    st.write("Counter value: ", st.session_state.count)

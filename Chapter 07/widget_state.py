import streamlit as st

with st.echo():
    import streamlit as st

    minimum = st.number_input("Enter the minimum value", 1)

    st.slider("Select a value", min_value=minimum, max_value=100)

    st.write(st.runtime.scriptrunner.get_script_run_ctx().session_state)

import streamlit as st

with st.echo():
    import streamlit as st

    def print_secrets(**secrets):
        st.write(secrets)

    st.header("All secrets")
    print_secrets(**st.secrets)

    st.header("database_1 secrets")
    print_secrets(**st.secrets.database_1)

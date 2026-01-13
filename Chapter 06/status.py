import streamlit as st

with st.echo():
    from time import sleep

    with st.status("Becoming a Streamlit master...", expanded=True) as status:
        st.write("Reading this book...")
        sleep(1)
        st.write("Running the examples...")
        sleep(1)
        st.write("Practicing what I've learned...")
        status.update(
            label="I am now a Streamlit master!", state="complete", expanded=False
        )
    st.button("Rerun")

import streamlit as st

with st.echo():
    import time

    my_bar = st.progress(0, text="Starting...")

    for percent_complete in range(100):
        my_bar.progress(
            percent_complete + 1,
            text="Done ✅"
            if percent_complete + 1 == 100
            else f"Progress: {percent_complete+1}%",
        )
        time.sleep(0.01)
    time.sleep(1)

    st.button("Rerun")

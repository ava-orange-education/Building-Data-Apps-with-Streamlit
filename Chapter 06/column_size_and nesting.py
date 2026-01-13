import streamlit as st

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor."

with st.echo():
    col1, col2, col3 = st.columns([1, 3, 2])

    with col1:
        st.write("__Column 1__")
        st.write("This column is `1/(1+3+2)` = 1/6th of the total width")

    with col2:
        st.write("__Column 2__")
        st.write(
            "This column is `3/(1+3+2)` = 1/2 of the total width, thrice the width of column 1"
        )

        col2_1, col2_2 = st.columns([2, 1])

        with col2_1:
            st.write("__Column 2.1__")
            st.write("This nested column is double the width of column 2.2")

            col2_1_1, col2_1_2 = st.columns(2)

            with col2_1_1:
                st.write("__Column 2.1.1__")
                st.write("This nested column is the same width as column 2.1.2")

            with col2_1_2:
                st.write("__Column 2.1.2__")
                st.write("This nested column is the same width as column 2.1.1")

        col2_2.write("__Column 2.2__")

    with col3:
        st.write("__Column 3__")
        st.write(
            "This column is `2/(1+3+2)` = 1/3rd of the total width, twice the width of column 1"
        )

import streamlit as st

with st.echo():
    with st.sidebar:
        st.header("This is the Sidebar")
        st.button("Settings")
        st.button("Logout")
        # Adding a selectbox for navigation options
        navigation_options = ["Dashboard", "Reports", "Analytics"]
        page = st.selectbox(
            "Navigate to:",
            options=navigation_options,
            placeholder="Select a page",
        )
        # Displaying the selected option
        if page != "Select a page":
            st.write(f"You selected {page}")

    st.title("This is the Main Canvas")

    # Displaying dynamic content based on sidebar navigation
    if page == "Dashboard":
        st.subheader("Dashboard")
        st.write("This is the dashboard page.")
    elif page == "Reports":
        st.subheader("Reports")
        st.write("Here you can view various reports.")
    elif page == "Analytics":
        st.subheader("Analytics")
        st.write("Analytics page provides insights into the data.")

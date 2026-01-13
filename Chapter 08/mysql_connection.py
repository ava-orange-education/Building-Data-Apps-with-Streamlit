import streamlit as st

if st.button("Connect"):
    connection = st.connection("mysql", type="sql")

    # Query data from the table
    query = st.text_area("Enter SQL query:", value="SELECT * FROM users;")
    if st.button("Run Query"):
        rows = connection.query(query, ttl=600)

        # Print the queried data
        for row in rows:
            st.write(row)

    # Close the connection
    if st.button("Close Connection"):
        connection.close()
        st.info("MySQL connection is closed")

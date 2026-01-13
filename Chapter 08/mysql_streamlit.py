import mysql.connector
import streamlit as st


@st.cache_resource
def connect_to_db(host: str, port: int, database: str, user: str, password: str):
    connection = mysql.connector.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password,
    )
    return connection


@st.cache_data
def query_data(connection, query: str):
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    return rows


# Connect to the MySQL database
host = st.text_input("Enter DB host:")
port = st.number_input("Enter DB port:", value=None)
database = st.text_input("Enter DB name:")
username = st.text_input("Enter DB username:")
password = st.text_input("Enter password", type="password")

if st.button("Connect"):
    connection = connect_to_db(
        host=host,
        port=port,
        database=database,
        user=st.secrets["DB_USERNAME"],
        password=st.secrets["DB_PASSWORD"],
    )

    st.success("Connected to MySQL database")

    # Query data from the table
    query = st.text_area("Enter SQL query:", value="SELECT * FROM users;")
    if st.button("Run Query"):
        rows = query_data(connection, query)

        # Print the queried data
        for row in rows:
            st.write(row)

    # Close the connection
    if st.button("Close Connection"):
        connection.close()
        st.info("MySQL connection is closed")


# .streamlit/secrets.toml
DB_USERNAME = "root"
DB_PASSWORD = "password"

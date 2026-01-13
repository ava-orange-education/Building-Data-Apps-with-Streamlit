import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    database="example_db",
    port=3306,
    user="root",
    password="password",
)

print("Connected to MySQL database")

# Create a cursor object
with connection.cursor() as cursor:
    # Query data from the table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Print the queried data
    for row in rows:
        print(row)

# Close the connection
connection.close()
print("MySQL connection is closed")

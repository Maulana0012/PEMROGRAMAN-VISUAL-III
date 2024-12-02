import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307"
)

print(database)
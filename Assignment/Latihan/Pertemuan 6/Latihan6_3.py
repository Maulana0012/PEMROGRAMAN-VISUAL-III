import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307"
)

myCursor = database.cursor()
myCursor.execute("CREATE DATABASE db_penjualan_visual")
print("Database Dibuat")
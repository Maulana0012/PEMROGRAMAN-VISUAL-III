import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307"
)

myCursor = database.cursor()
myCursor.execute("SHOW DATABASES")
for indexX in myCursor:
    print(indexX)

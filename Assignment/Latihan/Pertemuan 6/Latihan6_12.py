import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307",
    database="db_penjualan_visual"
)

myCursor = database.cursor()
myCursor.execute("SELECT * kategori")

result = myCursor.fetchone()

for indexX in result:
    print(indexX)
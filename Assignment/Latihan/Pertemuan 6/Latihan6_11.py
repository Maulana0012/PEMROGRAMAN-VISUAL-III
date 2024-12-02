import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307",
    database="db_penjualan_visual"
)

myCursor = database.cursor()
myCursor.execute("SELECT name FROM kategori")

result = myCursor.fetchall()

for indexX in result:
    print(indexX)
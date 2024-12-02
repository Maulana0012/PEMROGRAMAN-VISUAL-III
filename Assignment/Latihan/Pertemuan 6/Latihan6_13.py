import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307",
    database="db_penjualan_visual"
)

myCursor = database.cursor()
sqlSelect = ("SELECT * FROM kategori where id = '2'")
myCursor.execute(sqlSelect)
result = myCursor.fetchall()

for indexX in result:
    print(indexX)
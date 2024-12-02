import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307",
    database="db_penjualan_visual"
)

myCursor = database.cursor()
sqlSelect = ("SELECT * FROM kategori where id = %s")
id = ("4",)
myCursor.execute(sqlSelect, id)
result = myCursor.fetchall()

for indexX in result:
    print(indexX)
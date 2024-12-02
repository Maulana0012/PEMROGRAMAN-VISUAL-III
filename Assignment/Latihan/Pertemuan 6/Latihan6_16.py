import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307",
    database="db_penjualan_visual"
)

myCursor = database.cursor()
sqlSelect = ("DELETE FROM kategori where id = '4'")
myCursor.execute(sqlSelect)

database.commit()
print(myCursor.rowcount, "record(s) delete")
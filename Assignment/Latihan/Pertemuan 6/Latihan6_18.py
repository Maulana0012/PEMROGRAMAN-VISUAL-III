import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307",
    database="db_penjualan_visual"
)

myCursor = database.cursor()
sqlSelect = ("UPDATE kategori SET name = 'Jelly' where id = '3'")
myCursor.execute(sqlSelect)

database.commit()
print(myCursor.rowcount, "record(s) updated")
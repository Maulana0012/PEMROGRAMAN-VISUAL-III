import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307",
    database="db_penjualan_visual"
)

myCursor = database.cursor()
sqlInsert = "INSERT INTO kategori (id, name) VALUES " \
            "(""%s, %s)"
value = [("3", "Drinks"), ("4", "Tepung")]
myCursor.executemany(sqlInsert, value)

database.commit()
print(myCursor.rowcount, "Data Berhasil Ditambah")
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
value = ("5", "Roti")
myCursor.execute(sqlInsert, value)

database.commit()
print("1 record inserted, ID", myCursor.lastrowid)
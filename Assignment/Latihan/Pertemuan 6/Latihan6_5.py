import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307",
    database="db_penjualan_visual"
)

myCursor = database.cursor()
myCursor.execute("CREATE TABLE kategori("
                 "id int(9) primary key,"
                 "name varchar(50)"
                 ")")
print("berhasil ditambahkan")

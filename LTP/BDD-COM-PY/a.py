import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ifsp",
    database="petag"
)

Usuario = mydb.cursor()

Usuario.execute("SELECT * FROM Usuario")
myresult = Usuario.fetchall()

for x in myresult:
    print(x)
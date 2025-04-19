
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT \
employees.name AS employees, \
departments.name AS dept \
FROM mydatabase \
INNER JOIN departments ON employees. "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


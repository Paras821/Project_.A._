
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor(dictionary=True)

sql = ("SELECT name,joined FROM employees WHERE joined <= DATE_SUB(CURDATE(),INTERVAL 5 YEAR)")

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


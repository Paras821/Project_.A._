
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees)"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


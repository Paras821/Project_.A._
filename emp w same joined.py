
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT e1.id,e1.name,e1.joined FROM employees e1 WHERE EXISTS(SELECT 1 FROM employees e2 WHERE e2.joined = e1.joined AND e2.id != e1.id)"

mycursor.execute(sql)

myresult = mycursor.fetchall()

if myresult:
    print(f"ID:{x[0]}, Name:{x[1]}, Joined:{x[3]}")
else:
    print("No employees have joined the company in the same year")


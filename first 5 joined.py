
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT id, name, dept, joined FROM employees ORDER BY joined ASC LIMIT 5"

mycursor.execute(sql)

myresult = mycursor.fetchall()

if not myresult:
    print("No employees found")
else:
    print("First 5 employees who joined the company:")
    for x in myresult:
        print(f" ID: {x[0]} | Name: {x[1]} | Dept: {x[2]} | Joined: {x[3]}")


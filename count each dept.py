
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT dept, COUNT(id) FROM employees GROUP BY dept"

mycursor.execute(sql)

myresult = mycursor.fetchall()
print("Number of employees in each dept:")

for x in myresult:
    print(f" Dept: {x[0]} | Employees: {x[1]}")


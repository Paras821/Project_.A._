
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT * FROM employees WHERE dept = 'IT'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print("Employee(s) who belong to IT dept:")

for x in myresult:
    print(f" ID: {x[0]} | {x[1]}")



import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT * FROM employees WHERE name LIKE '%o%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print("Employee(s) whose name contains 'o':")

for x in myresult:
    print(f" ID: {x[0]} | {x[1]}")


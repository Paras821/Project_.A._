
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT * FROM employees WHERE age BETWEEN 25 AND 35"

mycursor.execute(sql)

myresult = mycursor.fetchall()
print("Employee(s) with age between 25 and 35:")

for x in myresult:
    print(f" ID: {x[0]} | Name: {x[1]} | Age: {x[2]}")


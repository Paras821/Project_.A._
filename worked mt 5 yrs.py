
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = ("SELECT id,name,joined FROM employees WHERE joined <= DATE_SUB(CURDATE(),INTERVAL 5 YEAR)")

mycursor.execute(sql)

myresult = mycursor.fetchall()

if myresult:
    print("Employees who have worked for more than 5 years:")
    for x in myresult:
        print(f" ID: {x[0]} | Name: {x[1]}")
else:
    print("No employees have worked for more than 5 years in the company")


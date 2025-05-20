
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT DISTINCT e.id, e.name, d.name FROM employees e JOIN departments d ON e.dept = d.name WHERE location = 'Paris'"

mycursor.execute(sql)

myresults = mycursor.fetchall()

if not myresults:
    print("No result found")
else:
    print("Employee(s) located in 'Paris':")
    for x in myresults:
        print(f" ID: {x[0]} | Name: {x[1]} | Department: {x[2]}")


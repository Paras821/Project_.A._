
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("DELETE e1 FROM employees e1 JOIN employees e2 ON e1.name = e2.name AND e1.age = e2.age AND e1.dept = e2.dept AND e1.salary = e2.salary AND e1.joined = e2.joined AND e1.id > e2.id")

myresult = mycursor.rowcount

if myresult:
    print(f" {myresult} deplicate records deleted")
else:
    print("No duplicate record(s) found")


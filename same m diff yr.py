
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT e1.id, e1.name, e1.joined FROM employees e1 WHERE EXISTS(SELECT 1 FROM employees e2 WHERE MONTH(e1.joined) = MONTH(e2.joined) AND YEAR(e1.joined) != YEAR(e2.joined))"

mycursor.execute(sql)

myresult = mycursor.fetchall()

if myresult:
    print("Employees who joined in the same month, but different years:")
    for x in myresult:
        print(f"Name: {x[0]}, Joined: {x[1]}")
else:
    print("No employees have joined the company in the same month across different years")


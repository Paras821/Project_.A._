
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT e.* FROM employees e LEFT JOIN promotions p ON e.id = p.employee_id WHERE p.emplyee_id IS NULL"

mycursor.execute(sql)

myresults = mycursor.fetchall()

if not myresults:
    print("All employees have been promoted")
else:
    for x in myresults:
        print(x)


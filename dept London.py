
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT DISTINCT e.dept, e.name AS employee_name FROM employees e JOIN departments d ON e.dept = d.name WHERE d.location = 'London'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(f" {x[1]} works in the {x[0]} dept located in London")


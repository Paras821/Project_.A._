
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = " SELECT dept, e.name AS employee_name FROM employees e JOIN departments ON dept WHERE location = 'London' "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)



import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT e.dept, e.name, e.age FROM employees e JOIN (SELECT dept, MAX(age) AS max_age FROM employees GROUP BY dept) AS sub ON e.dept = sub.dept AND e.age = sub.max_age"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for dept,name,age in myresult:
    print(f"In the {dept} dept, the oldest employee is {name}, aged {age}")


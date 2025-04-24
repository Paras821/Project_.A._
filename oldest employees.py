
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT dept,name,age FROM employees WHERE (dept, age) IN (SELECT dept,MAX(age) FROM employees GROUP BY dept)"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for dept,name,age in myresult:
    print(f"In the {dept} dept, the oldest employee is {name}, aged {age}")


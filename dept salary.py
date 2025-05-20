
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT dept, SUM(salary) FROM employees GROUP BY dept"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(f"Dept: {x[0]} | Total Salary: Rs.{x[1]}")


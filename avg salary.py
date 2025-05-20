
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT AVG(salary) FROM employees"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    avg = x[0]
    print(f"Average Salary: Rs.{int(avg)}")


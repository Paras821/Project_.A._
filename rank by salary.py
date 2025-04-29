
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT id, name, salary, RANK() OVER(ORDER BY salary DESC) AS salary_rank FROM employees "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(f"ID: {x[0]}, Name: {x[1]}, Salary: {x[2]}, Rank: {x[3]}")


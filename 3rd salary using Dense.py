
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT id, name, salary FROM (SELECT id, name, salary, DENSE_RANK() OVER(ORDER BY salary DESC) AS salary_rank FROM employees) ranked WHERE salary_rank = 3"

mycursor.execute(sql)

myresult = mycursor.fetchall()
print("Employee who earns the 3rd highest salary:")

for x in myresult:
    print(f" ID: {x[0]} | Name: {x[1]} | Salary: Rs.{x[2]}")


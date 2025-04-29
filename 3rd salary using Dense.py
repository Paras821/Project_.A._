
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT name, salary FROM(SELECT name, salary, DENSE_RANK() OVER(ORDER BY salary DESC) AS salary_rank FROM employees) ranked WHERE salary_rank = 3"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for name, salary in myresult:
    print(f"Name: {name}, Salary: RS.{salary}")


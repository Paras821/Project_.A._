
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "WITH ranked_employees AS (SELECT id, name, salary, RANK() OVER(ORDER BY salary DESC) AS salary_rank FROM employees) SELECT * FROM ranked_employees ORDER BY salary_rank"

mycursor.execute(sql)

myresult = mycursor.fetchall()
print("Employees ranked based on their salary:")

for x in myresult:
    print(f"  Rank: {x[3]} - ID: {x[0]} | Name: {x[1]} | Salary: Rs.{x[2]}")



import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT id,name, salary FROM employees WHERE salary = (SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1)"

mycursor.execute(sql)

myresult = mycursor.fetchall()
print("Second highest salary in the company:")

for x in myresult:
    print(f" Salary: Rs.{x[2]} | Name: {x[1]} | ID: {x[0]}")


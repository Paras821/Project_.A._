
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT d.name, e.num_employees FROM departments d JOIN (SELECT dept, COUNT(*) AS num_employees FROM employees GROUP BY dept ORDER BY num_employees DESC LIMIT 1) e ON d.name = e.dept"

mycursor.execute(sql)

myresult = mycursor.fetchone()

if myresult:
    dept_name, employee_count = myresult
    print(f"Dept with the highest number of employees: {dept_name} ({employee_count} employees)")
else:
    print("No data found")


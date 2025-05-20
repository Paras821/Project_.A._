
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT d.name, e.num_employees FROM departments d JOIN (SELECT dept, COUNT(*) AS num_employees FROM employees GROUP BY dept) e ON d.name = e.dept WHERE e.num_employees = (SELECT MAX(dept_count) FROM (SELECT COUNT(*) AS dept_count FROM employees GROUP BY dept) AS counts)"

mycursor.execute(sql)

myresult = mycursor.fetchone()

if myresult:
    dept_name, employee_count = myresult
    print(f"Dept with the highest number of employees: {dept_name} ({employee_count} employees)")
else:
    print("No data found")


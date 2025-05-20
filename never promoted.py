
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT e.id, e.name, e.dept, CASE  WHEN p.emp_id IS NOT NULL THEN 'Promoted' ELSE 'Not Promoted' END AS promotion_status FROM employees e LEFT JOIN promotions p ON e.id = p.emp_id GROUP BY e.id, e.name, e.dept"

mycursor.execute(sql)

myresults = mycursor.fetchall()

print("Employee Promtion Status:")

for x in myresults:
    print(f" ID: {x[0]} | Name: {x[1]} | Dept: {x[2]} -- {x[3]}")


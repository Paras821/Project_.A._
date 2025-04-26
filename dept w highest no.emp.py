
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT name FROM departments JOIN (SELECT dept, COUNT(*) as num_employees FROM employees GROUP BY id,dept ORDER BY num_employees DESC LIMIT 1) e ON id"

mycursor.execute(sql)

myresult = mycursor.fetchone()

if myresult:
    print(f"Dept with the highest number of employees: {myresult[0]}")
else:
    print("No data found")


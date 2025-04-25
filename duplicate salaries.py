
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT salary, COUNT(*) as count FROM employees GROUP BY salary HAVING COUNT(*) > 1"

mycursor.execute(sql)

myresult = mycursor.fetchall()

if not myresult:
    print("No duplicate salaries found")
else:
    print("Duplicate salaries:")
    for salary, count in myresult:
        print(f"Salary:{salary}, Count:{count}")


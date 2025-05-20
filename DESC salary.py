
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT * FROM employees ORDER BY salary DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print("Employees sorted by their salaries in descending order:")

for x in myresult:
    print(f" ID: {x[0]} | {x[1]} | {x[2]} years | {x[3]} dept | Rs.{x[4]} salary | Joined on {x[5]}")


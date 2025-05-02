
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT e.id, e.name, e.dept, e.joined FROM employees e INNER JOIN (SELECT dept, MIN(joined) AS first_to_join FROM employees GROUP BY dept) first_joined ON e.dept = first_joined.dept AND e.joined = first_joined.first_to_join"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(f"Employee ID: {x[0]}, Name: {x[1]}, Dept: {x[2]}, Joined: {x[3]}")


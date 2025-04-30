
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT name, dept, joined FROM employees ORDER BY joined LIMIT 5"

mycursor.execute(sql)

myresult = mycursor.fetchall()

if not myresult:
    print("No employees found")
else:
    for x in myresult:
        name, dept, joined = x
        print(f"Name: {name} | Department: {dept} | Joined: {joined}")


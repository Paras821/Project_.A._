
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM employees")

myresult = mycursor.fetchall()

print("Employees:")

for x in myresult:
    print(f" {x[0]} : {x[1]} | {x[2]} yrs | {x[3]} dept | Rs.{x[4]} salary | Joined on {x[5]}")


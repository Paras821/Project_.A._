
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT * FROM employees WHERE joined > '2020-12-31'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print("Employee(s) who joined after the year 2020:")

for x in myresult:
    print(f" ID: {x[0]} | {x[1]} | Joined on {x[5]}")


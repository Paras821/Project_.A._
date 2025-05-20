
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT * FROM employees WHERE joined > DATE_ADD((SELECT MIN(joined) FROM employees), INTERVAL 2 YEAR)"

mycursor.execute(sql)

myresult = mycursor.fetchall()
print("Employee(s) who joined in last 2 years")

for x in myresult:
    print(f" ID: {x[0]} | Name: {x[1]} | Joined: {x[5]}")


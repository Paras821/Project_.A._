
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT * FROM employees WHERE dept != 'HR' ORDER BY dept DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print("Employee(s) who are Not in the HR dept: \n")

for x in myresult:
    print(f" Dept: {x[3]} | ID: {x[0]} | Name: {x[1]} ")


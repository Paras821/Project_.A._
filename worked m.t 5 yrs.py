
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = ("SELECT name,joined FROM employees WHERE joined < DATE(2020-04-25) GROUP BY name,joined")

mycursor.execute(sql)

myresult = mycursor.fetchall()

if not myresult:
    print("No Employees")
else:
    print("4 Employees", myresult)

##


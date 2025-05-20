
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT d.name FROM departments d LEFT JOIN employees e ON d.name = e.dept WHERE e.id IS NULL"

mycursor.execute(sql)

myresult = mycursor.fetchall()

if myresult:
    for x in myresult:
        print(f"Dept '{x[0]}' has no employees assigned")
else:
    print("All departments have employee(s) assigned")


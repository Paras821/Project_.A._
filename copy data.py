
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("DROP TABLE IF EXISTS employees_backup")

mycursor.execute("CREATE TABLE employees_backup AS SELECT * FROM employees")
print("The data has been copied to the table 'employees_backup'\n")

mycursor.execute("SELECT * FROM employees_backup")
myresult = mycursor.fetchall()
print("Data:")

for x in myresult:
    print(f" ID: {x[0]} | Name: {x[1]} | Age: {x[2]} | Dept: {x[3]} | Salary: Rs.{x[4]} | Joined: {x[5]}")


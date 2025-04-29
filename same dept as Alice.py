
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("SELECT dept FROM employees WHERE name = 'Alice'")
myresult = mycursor.fetchall()

if myresult:
    dept = myresult[0][0]

    mycursor.execute("SELECT name FROM employees WHERE dept = %s AND name != 'Alice'", (dept,))
    coworkers = mycursor.fetchall()

    if coworkers:
        print("Employees in the same department as Alice:")
        for (name,) in coworkers:
            print(f" {name}")
    else:
        print("No employees in the same department as Alice")

else:
    print("Alice not found")



import mysql.connector

emp = "Alice"

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("SELECT dept FROM employees WHERE name = %s", (emp,))
myresult = mycursor.fetchone()

if myresult:
    dept = myresult[0]

    mycursor.execute("SELECT name FROM employees WHERE dept = %s AND name != %s", (dept, emp))
    coworkers = mycursor.fetchall()

    if coworkers:
        print(f"Employee(s) in the same department as {emp}:")
        for (name,) in coworkers:
            print(f" {emp}")
    else:
        print(f"No employee works in the same department as {emp}")

else:
    print(f"{emp} not found")


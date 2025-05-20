
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("SELECT salary FROM employees WHERE name = 'Alice'")
alice_salary = mycursor.fetchone()[0]

mycursor.execute("SELECT salary FROM employees WHERE name = 'Bob'")
bob_salary = mycursor.fetchone()[0]

mycursor.execute("UPDATE employees SET salary = %s WHERE name = 'Alice'",(bob_salary,))
mycursor.execute("UPDATE employees SET salary = %s WHERE name = 'Bob'",(alice_salary,))

mycursor.execute("SELECT id, name, salary FROM employees WHERE name IN('Alice', 'Bob')")

for x in mycursor.fetchall():
    print(f" ID: {x[0]} | Name: {x[1]}| Salary: Rs.{x[2]}")


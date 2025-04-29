
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 3"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print("Top 3 highest-paid employees:")

for name, salary in myresult:
    print(f" {name}: Rs.{salary:,}")


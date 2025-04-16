
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "UPDATE employees SET salary = 65000 WHERE salary = 60000"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "Record(s) Updated")


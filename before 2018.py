
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "DELETE FROM employees WHERE joined < '2018-11-23'"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "Record(s) Deleted")


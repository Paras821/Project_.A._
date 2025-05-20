
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("ALTER TABLE employees ADD COLUMN bonus INT")

conn.commit()

print("Column 'bonus' added successfully")


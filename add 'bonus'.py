
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("ALTER TABLE employees ADD COLUMN bonus INT AUTO_INCREMENT PRIMARY KEY")

conn.commit()

print("Row Added Successfully")


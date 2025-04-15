
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

sql = "INSERT INTO departments(id,name,location) VALUES (%s, %s, %s)"
val = [
    ('1', 'HR', 'NY'),
    ('2', 'IT', 'London'),
    ('3', 'Finance', 'Paris')
    ]

mycursor.executemany(sql,val)

conn.commit()

print(mycursor.rowcount, "Record(s) Inserted")



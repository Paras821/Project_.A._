
import mysql.connector

conn = mysql.connector.MySQLConnection(host="localhost", user="root", password="Root@123", database="mydatabase")

mycursor = conn.cursor()

mycursor.execute("WITH ranked_employees AS (SELECT id, ROW_NUMBER() OVER (PARTITION BY name, dept, salary ORDER BY id) AS rn FROM employees) DELETE FROM employees WHERE id IN (SELECT id FROM ranked_employees WHERE rn > 1)")

myresult = mycursor.fetchall()

if myresult:
    print(f"{cursor.rowcount} deplicate records deleted")
else:
    print("No duplicate records found")


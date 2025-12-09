import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="university"
)

cursor = connection.cursor()

cursor.execute("DESCRIBE students;")
rows = cursor.fetchall()

print("Структура таблиці 'students':")
for row in rows:
    print(row)

cursor.close()
connection.close()

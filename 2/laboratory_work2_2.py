import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="university"
)

cursor = connection.cursor()

query = """
SELECT group_name, COUNT(*) AS student_count, AVG(age) AS avg_age
FROM students
WHERE age > 18
GROUP BY group_name
HAVING AVG(age) > 19;
"""

cursor.execute(query)

rows = cursor.fetchall()

print("Групи, де середній вік студентів (старших 18) більший за 19:")
for row in rows:
    print(row)

cursor.close()
connection.close()

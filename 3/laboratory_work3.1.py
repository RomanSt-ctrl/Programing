import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS cinema;")

cursor.execute("USE cinema;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS films (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    year INT,
    rating FLOAT
);
""")

cursor.execute("CREATE USER IF NOT EXISTS 'films_admin'@'localhost' IDENTIFIED BY 'films123';")

cursor.execute("GRANT INSERT, UPDATE, DELETE ON cinema.* TO 'films_admin'@'localhost';")

cursor.execute("FLUSH PRIVILEGES;")

print("База, таблиця і користувач успішно створені!")

cursor.close()
connection.close()

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cinema"
)

cursor = connection.cursor()

insert_query = """
INSERT INTO films (title, genre, year, rating) VALUES
    ('Inception', 'Sci-Fi', 2010, 8.8),
    ('Interstellar', 'Sci-Fi', 2014, 8.6),
    ('Titanic', 'Drama', 1997, 7.8),
    ('Avatar', 'Sci-Fi', 2009, 7.9),
    ('The Godfather', 'Crime', 1972, 9.2);
"""
cursor.execute(insert_query)
connection.commit()
print("Фільми вставлено!")

update_query = """
UPDATE films
SET rating = 9.0
WHERE title = 'Interstellar';
"""
cursor.execute(update_query)
connection.commit()
print("Дані фільму оновлено!")

delete_query = """
DELETE FROM films
WHERE title = 'Titanic';
"""
cursor.execute(delete_query)
connection.commit()
print("Один фільм видалено!")

select_query = """
SELECT genre, COUNT(*) AS film_count, AVG(rating) AS avg_rating
FROM films
GROUP BY genre;
"""
cursor.execute(select_query)
rows = cursor.fetchall()

print("\nГрупування за жанром:")
for row in rows:
    print(f"Жанр: {row[0]}, Кількість фільмів: {row[1]}, Середній рейтинг: {row[2]:.2f}")

cursor.close()
connection.close()

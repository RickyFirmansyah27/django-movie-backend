import psycopg2
import json

conn = psycopg2.connect(
    "postgresql://neondb_owner:npg_rNbUM3kWw0ZB@ep-green-forest-a5wzvqzd-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require"
)

cur = conn.cursor()

with open('movies.json', 'r') as file:
    movies_data = json.load(file)

insert_query = """
    INSERT INTO movies (name, description, imgPath, duration, genre, language, mpaaRating, userRating)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

for movie in movies_data:
    name = movie.get("name")
    description = movie.get("description")
    imgPath = movie.get("imgPath")
    duration = movie.get("duration")
    genre = movie.get("genre")
    language = movie.get("language")
    mpaaRating = json.dumps(movie.get("mpaaRating"))
    userRating = movie.get("userRating")
    
    # Eksekusi query insert
    cur.execute(insert_query, (name, description, imgPath, duration, genre, language, mpaaRating, userRating))

conn.commit()
cur.close()
conn.close()

print("Data berhasil dimasukkan ke dalam tabel.")

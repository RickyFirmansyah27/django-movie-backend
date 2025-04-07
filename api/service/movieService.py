from api.config.dbConnection import execute_sql_query

def getMovies():
    try:
        movies = execute_sql_query('SELECT * FROM movies')

        movie_list = []
        for movie in movies:
            movie_dict = {
                "id": movie[0],
                "name": movie[1],
                "description": movie[2],
                "imgPath": movie[3],
                "duration": movie[4],
                "genre": movie[5],
                "language": movie[6],
                "mpaaRating": movie[7],
                "userRating": movie[8]
            }
            movie_list.append(movie_dict)

        return movie_list
    except Exception as err:
        raise Exception(f"Error fetching movies: {str(err)}")

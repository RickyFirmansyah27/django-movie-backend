from api.helper import dbQuery
import logging

# Configure logging
logger = logging.getLogger('info')

def getMovies(params):
    logger.info(f'[MoviesService] - payload: {params}')
    try:
        movies = dbQuery.get_all_movies(params)

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

        logger.info(f'[MoviesService] - end')
        return movie_list
    except Exception as err:
        logger.info(f'[MoviesService] - erorr: {err}')
        raise Exception(f"Error fetching movies: {str(err)}")

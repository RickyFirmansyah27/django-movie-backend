import logging
from rest_framework.decorators import api_view
from api.response.helper import BaseResponse
from api.service import movieService

# Configure logging
logger = logging.getLogger('response')


@api_view(['GET'])
def getMovies(request):
    try:
        # Data sampel
        movies = movieService.getMovies()

        logger.info(f'[MoviesController] - Fetched all movie successfully. {movies}')

        return BaseResponse('success', 'Successfully fetched sample movies', movies)
    except Exception as e:
        logger.error('[MoviesController] - Failed to fetch sample movies.', exc_info=True)
        return BaseResponse('error', 'Failed to fetch sample movies', str(e))

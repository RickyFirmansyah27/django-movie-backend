import logging
from rest_framework.decorators import api_view
from api.response.helper import BaseResponse
from api.service import movieService

# Configure logging
logger = logging.getLogger('response')


@api_view(['GET'])
def getMovies(request):
    try:
        query_params = request.GET.dict()
        print(query_params)

        movies = movieService.getMovies(query_params)

        logger.info(f'[MoviesController] - Fetched movies successfully with params: {query_params}')

        return BaseResponse('success', 'Successfully fetched movies', movies)
    except Exception as e:
        logger.error('[MoviesController] - Failed to fetch movies.', exc_info=True)
        return BaseResponse('error', 'Failed to fetch movies', str(e))
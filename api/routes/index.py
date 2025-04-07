# api/routes/index.py
from django.urls import path
from api.controller import movieController

urlpatterns = [
    path('api/movies/', movieController.getMovies, name='get movies data'),
]

# api/routes/index.py
from django.urls import path
from api.controller import movieController

urlpatterns = [
    path('', movieController.getMovies, name='get movies data'),
]

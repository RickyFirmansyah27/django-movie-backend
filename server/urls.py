from django.urls import path, include, re_path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('api/', include('api.routes.index')),
]

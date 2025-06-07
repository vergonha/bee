from django.urls import path
from .views import movie_view

app_name = "movies"

urlpatterns  = [
    path('', movie_view.index),
    path('api/search', movie_view.search),
    path('api/movie', movie_view.create),
    path('api/all', movie_view.all),
    path('api/df', movie_view.dataframe)
]


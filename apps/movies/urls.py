from django.urls import path
from .views import movie_view

app_name = "movies"

urlpatterns  = [
    path('/', movie_view.movie_list),
]


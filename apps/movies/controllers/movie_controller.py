import json
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import JsonResponse, Http404
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
from django.core import serializers

from ..models.movie import Movie
from ..services.database.movie import MovieService

from ..services.imdb import ImdbRequests
from ..services.imdb import ImdbScraping

class MovieController:
    
    @staticmethod
    def index(request):
        return render(request, "movies/index.html")
    
    @staticmethod
    def search(query):
        return JsonResponse(ImdbRequests.search(query[0]), safe=False)
    
    @staticmethod
    def all(request):
        # https://docs.djangoproject.com/en/5.2/topics/serialization/
        return JsonResponse(list(Movie.objects.all().values()), safe=False)
    
    @staticmethod
    def create_movie(request):
        try:
            body = json.loads(request.body)

            id = body.get('id', '').strip()
            data = ImdbScraping.get_movie(id)

            movie = MovieService.create_movie(data)
            messages.success(request, f'Movie "{movie.name}" created successfully!')
            return JsonResponse({"success": True, "movie": data})
            
        except (ValueError, ValidationError) as e:
            messages.error(request, f'Error creating movie: {str(e)}')
            return JsonResponse({"success": False})
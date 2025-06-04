
import json
from django.http import JsonResponse, Http404
from django.core.serializers.json import DjangoJSONEncoder

from ..services import MovieService

class MovieController:
    
    @staticmethod
    def index(request):
        movies = MovieService.get_all_movies()
            
        
        context = {
            'movies': json.dumps(list(movies), cls=DjangoJSONEncoder),
        }

        print(context)
        return JsonResponse(context)
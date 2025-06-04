from django.core.exceptions import ValidationError
from django.db.models import Q
from ..models import Movie

class MovieService:
    
    @staticmethod
    def get_all_movies():
        return Movie.objects.all().order_by('-created_at')
    
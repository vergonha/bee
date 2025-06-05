from django.core.exceptions import ValidationError
from django.db.models import Q
from ...models.movie import Movie

class MovieService:
   @staticmethod
   def create_movie(data):
        valid_fields = [field.name for field in Movie._meta.get_fields()]
        # Parece que o Model do Django não aceita que eu envie mais campos do que deveria.
        # Isso evita que meu programa quebre
        filtered_data = {k: v for k, v in data.items() if k in valid_fields and v is not None}
        
        movie = Movie(**filtered_data)
        try:
            movie.full_clean()  
            movie.save()
            return movie
        except ValidationError as e:
            raise ValidationError(f"Movie creation failed: {e}")
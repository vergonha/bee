import requests
from datetime import datetime

class ImdbRequests():

  def _parse_movie_data(data):
    movies = []

    for item in data.get('d', []):
        movie = {
            'id': item.get('id'),
            'name': item.get('l', 'Unknown Title'),
            'description': item.get('q', 'No description available'),
            'cover': item.get('i', {}).get('imageUrl', ''),
            'rating': None,  # Não tem :(
            'release_date': None,  # Não tem nessa API.
            'created_at': datetime.now(),  
            'updated_at': datetime.now(),
        }

        movies.append(movie)
    
    return movies

  @staticmethod
  def search(query):
    response = requests.get("https://v3.sg.media-imdb.com/suggestion/x/" + query + ".json")
    
    if(response.status_code != 200):
      return {}

    return ImdbRequests._parse_movie_data(response.json())
  


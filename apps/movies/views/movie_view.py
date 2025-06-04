from ..controllers import MovieController

def movie_list(request):
    return MovieController.index(request)
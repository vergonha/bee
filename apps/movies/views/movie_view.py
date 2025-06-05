from ..controllers import MovieController

def index(request):
    return MovieController.index(request)


def search(request):
    return MovieController.search(dict(request.GET)['q'])

def all(request):
    return MovieController.all(request)

def create(request):
   if request.method == 'POST':
    return MovieController.create_movie(request)
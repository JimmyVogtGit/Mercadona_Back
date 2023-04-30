from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Salut Alison, je pense fort à toi !!!</h1>")
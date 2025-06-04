from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> Bonjour </h1>")

def dashboard(request):
    return HttpResponse("<h1> dashboard page </h1>")
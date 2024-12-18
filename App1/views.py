from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    content = "<h1> Bienvenue sur Django ! </h1>"
    return HttpResponse(content)

def contact(request):
    content = "<form>Mail : <input type='mail' "
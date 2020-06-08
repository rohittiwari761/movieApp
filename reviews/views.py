from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from imdb import IMDb
from .models import Genres
import requests
# Create your views here.
def index(request):
    name='inception'
    if request.method == 'POST':
        name = request.POST['MovieName']
    ia = IMDb()
    movie = ia.search_movie(name)
    for i in movie:
        i.update({'ID':i.getID,'poster':i['full-size cover url']})
    context={
    'movies':movie,
    'genres':Genres.objects.all(),
    }
    return render(request,'review/index.html',context)


def search(request,id):
    id=int(id)
    ia=IMDb()
    movie=ia.get_movie(id)
    movie['cover_poster'] = movie['full-size cover url']
    movie['language'] = movie.pop('language codes')
    try:
        movie['release']=movie.pop('original air date')
    except KeyError:
        movie['release']=movie.pop('series years')
    context={
    'movies':movie,
    'genres':Genres.objects.all(),
    }
    return render(request,'review/movie.html',context)
def user(request):
    return render(request,'review/user.html')

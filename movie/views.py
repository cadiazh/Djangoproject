from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.

def home(request):
    #return HttpResponse('<h1>hi welcome to the page</h1>')
    #return render(request,'home.html')
    #return render(request,'home.html',{'name':'Arturo Diaz'})
    searchterm = request.GET.get('searchMovie')
    if searchterm:
        movies = Movie.objects.filter(title__icontains=searchterm)
    else:
        movies = Movie.objects.all()
    return render(request,'home.html', {'searchTerm': searchterm, 'movies': movies})

def about(request):
    return render(request,'about.html')
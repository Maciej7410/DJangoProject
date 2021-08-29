from django.shortcuts import render


from django.views.generic import ListView, FormView
# from django.http import HttpResponse

# Create your views here.
from viewer.models import Movie

from viewer.forms import MovieForm

class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie

class MovieCreateView(FormView):
    template_name = 'form.html'
    form_class = MovieForm
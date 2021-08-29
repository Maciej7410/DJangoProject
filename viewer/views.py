from django.shortcuts import render

from django.views.generic import ListView, FormView, CreateView, UpdateView
# from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.
from viewer.models import Movie

from viewer.forms import MovieForm

from logging import getLogger

LOGGER = getLogger()


class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie


class MovieCreateView(CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    # adres pobrany z URL-s na który zostaniemy przekierowani gdy walidacja się powiedzie
    # (movie_create pochodzi z name!) reverse_lazy pochodzi z djago.urls
    success_url = reverse_lazy('movie_create')

    # co ma się wydarzyć gdy formularz przeszedł walidację:

    # co ma się wydarzyć gdy formularz nie przeszedł walidacji:
    def form_invalid(self, form):
        # odkładamy w logach informacje o operacji
        LOGGER.warning('User provided invalid data')
        # zwracamy wynik działania pierwotnej funkcji form_invalid
        return super().form_invalid(form)


class MovieUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = MovieForm
    # adres pobrany z URL-s na który zostaniemy przekierowani gdy aktualizacja się powiedzie
    # (movie_create pochodzi z name!) reverse_lazy pochodzi z djago.urls
    success_url = reverse_lazy('index')
    model = Movie

    # co ma się wydarzyć gdy formularz nie przeszedł update:
    def form_invalid(self, form):
        # odkładamy w logach informacje o operacji
        LOGGER.warning('User provided invalid data when updating')
        # zwracamy wynik działania pierwotnej funkcji form_invalid
        return super().form_invalid(form)

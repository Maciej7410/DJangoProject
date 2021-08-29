from django.shortcuts import render


from django.views.generic import ListView, FormView
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


class MovieCreateView(FormView):
    template_name = 'form.html'
    form_class = MovieForm
    # adres pobrany z URL-s na który zostaniemy przekierowani gdy walidacja się powiedzie
    # (movie_create pochodzi z name!) reverse_lazy pochodzi z djago.urls
    success_url = reverse_lazy('movie_create')

    # co ma się wydarzyć gdy formularz przeszedł walidację:
    def form_valid(self, form):
        # wywołanie metody form_valid z klasy nadrzędnej (FormView)
        # będziemy zwracać wynik z niej uzyskany
        result = super().form_valid(form)
        # w obiekcie cleaned_datea przechowujemy wynik działania funkcji czyszczących clean
        cleaned_data = form.cleaned_data
        # Zapisujemy do bazy nowy film:
        Movie.objects.create(
            title       =cleaned_data['title'],
            genre       =cleaned_data['genre'],
            rating      =cleaned_data['rating'],
            released    =cleaned_data['released'],
            description = cleaned_data['description'],
        )
        # zwracamy result - komentarz z ini 32
        return result


    # co ma się wydarzyć gdy formularz nie przeszedł walidacji:
    def form_invalid(self, form):
        # odkładamy w logach informacje o operacji
        LOGGER.warning('User provided invalid data')
        # zwracamy wynik działania pierwotnej funkcji form_invalid
        return super().form_invalid(form)

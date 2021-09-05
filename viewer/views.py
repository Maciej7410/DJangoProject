from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
# from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.
from viewer.models import Movie

from viewer.forms import MovieForm

from logging import getLogger
import datetime

LOGGER = getLogger()

from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def generate_demo(request):
    our_get = request.GET.get('name', '')
    return render(
        request, template_name='demo.html',
        context={'our_get': our_get,
                 'list': ['pierwszy', 'drugi', 'trzeci', 'czwarty'],
                 'nasza_data': datetime.datetime.now()
                 }

    )


class MoviesView(LoginRequiredMixin, ListView):
    template_name = 'movies.html'
    model = Movie




class MovieCreateView(LoginRequiredMixin,CreateView):
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


class MovieUpdateView(LoginRequiredMixin, UpdateView):
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


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    # nazwa szablonu wraz z rozszerzeniem którą pobieramy z folderu templates
    template_name = 'delete_movie.html'
    # nazwa encji z której będziemy kasować rekord
    model = Movie
    success_url = reverse_lazy('index')

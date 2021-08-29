from django.shortcuts import render

# from django.http import HttpResponse
from django.views import View
# Create your views here.
from viewer.models import Movie

class MoviesView(View):
    def get(self, request):
        return render(
            request, template_name='movies.html',
            context={
                'movies': Movie.objects.all()
            }
        )

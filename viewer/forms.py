from django.forms import (
    Form, CharField, ModelChoiceField, IntegerField, DateField, Textarea, ModelForm
)
from viewer.validators import PastMonthField, capitalized_validator
from django.core.exceptions import ValidationError
from viewer.models import Genre, Movie
import re
class MovieForm(ModelForm):
    class Meta:
        model = Movie # model na podstawie tworzymy formularz
        fields = '__all__' # wykorzystujemy wszystkie pola z modelu

    # pola z własnymi walidatorami dodajemy oddzielnie poa META
    title = CharField(validators=[capitalized_validator])
    rating = IntegerField(min_value=1, max_value=10)
    released = PastMonthField()

    def clean_description(self):
        # pobranie wartości pola description
        initial = self.cleaned_data['description']
        # podział tekstu na części "od kropki do kropki" - na zdania
        sentences = re.sub(r'\s*\.\s*','.',initial).split('.')
        # zamiana na wielką literę pierwszej litery każdego ze zdań,
        # dodanie kropki, powtórzenie operacji dla kolejnego zdania
        return '.'.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'comedy' and result['rating'] > 7:
            self.add_error('genre','tresc wiadomości') # oznaczenie pola jako błedne z komentarze tresc..
            self.add_error('rating','tresc rating')
            # rzucamy ogólny błąd / wyjątek
            raise ValidationError(
                'Comedies aren\'t so good to be over 7'
            )
        return result

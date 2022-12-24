from django import forms
from django import forms
from .models import CD, GENRE_CHOICES

class ExchangeForm(forms.Form):
    class Meta:
        model = CD
        fields = ('name', 'email', 'title', 'artist', 'genre', 'price', 'comment')

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    title = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=40)
    genre = forms.ChoiceField(choices = GENRE_CHOICES)
    price = forms.DecimalField(required = False)
    comment = forms.CharField(widget=forms.Textarea)
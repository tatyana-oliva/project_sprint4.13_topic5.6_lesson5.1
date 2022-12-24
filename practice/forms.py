from django import forms
#from django.db import models
from django import forms
from .models import CD #, GENRE_CHOICES

class ExchangeForm(forms.Form):
    class Meta:
        model = CD
        fields = ('name', 'email', 'title', 'artist', 'genre', 'price', 'comment')
        
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    title = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=40)
    # genre = поле выбора из предустановленных значений.
    #genre = forms.ChoiceField(choices = GENRE_CHOICES)
    # price = числовое поле, десятичные числа; необязательное.
    price = forms.DecimalField(required = False)
    # comment = многострочное текстовое поле; необязательное.
    comment = forms.CharField(widget=forms.Textarea)
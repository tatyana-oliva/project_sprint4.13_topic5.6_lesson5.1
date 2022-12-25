from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
# from .models import ExchangeModel
from .forms import ExchangeForm

def send_msg(email, name, title, artist, genre, price, comment):
    subject = f"Обмен {artist}-{title}"
    body = f"""Предложение на обмен диска от {name} ({email})

    Название: {title}
    Исполнитель: {artist}
    Жанр: {genre}
    Стоимость: {price}
    Комментарий: {comment}

    """
    send_mail(
        subject, body, email, ["admin@rockenrolla.net", ],
    )

def thankyou(request):
    return render(request, 'thankyou.html', {})

def index(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)

        if form.is_valid():
            cleaned_form = form.cleaned_data

            # cd = ExchangeModel()
            # cd.name = cleaned_form["name"]
            # cd.email = cleaned_form["email"]
            # cd.title = cleaned_form["title"]
            # cd.artist = cleaned_form["artist"]
            # cd.genre = cleaned_form["genre"]
            # cd.price = cleaned_form["price"]
            # cd.comment = cleaned_form["comment"]
            # cd.save()

            name = cleaned_form["name"]
            email = cleaned_form["email"]
            title = cleaned_form["title"]
            artist = cleaned_form["artist"]
            genre = cleaned_form["genre"]
            price = cleaned_form["price"]
            comment = cleaned_form["comment"]
            send_msg(email, name, title, artist, genre, price, comment)

            # return render(request, 'thankyou.html')
            return redirect('/thank-you/')

        return render(request, 'index.html', {'form': form})

    # После заполнения формы показывайте шаблон "thankyou.html"
    form = ExchangeForm()
    return render(request, 'index.html', {'form': form})

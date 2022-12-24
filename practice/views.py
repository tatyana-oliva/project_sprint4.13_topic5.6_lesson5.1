from django.shortcuts import render
from django.core.mail import send_mail
from .models import CD
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


def index(request):
    # После заполнения формы показывайте шаблон "thankyou.html"
    form = ExchangeForm()
    return render(request, 'index.html', {'form': form})

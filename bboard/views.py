from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb

def index(request):
    list = 'Список объявлений\r\n\r\n\r\n'
    for b in Bb.objects.order_by('-published'):
        list += str(b.id) + ' ' + b.title + '\r\n' + b.content + '  Опубликовано: ' + str(b.published) + '\r\n\r\n'
    return HttpResponse(list, content_type = 'text/plain; charset=utf-8')


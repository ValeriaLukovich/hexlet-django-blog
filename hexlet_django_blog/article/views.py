from django.shortcuts import render

from django.http import HttpResponse

NAME_APP = 'Hexlet-Django-Blog'
def index(request):
    return render(request, 'articles/index.html', context={
        'name': NAME_APP,
    })

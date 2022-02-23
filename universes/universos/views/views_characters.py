from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from universos.models import *


# Create your views here.


def listMarvel(request):
    list = Character.objects.filter(universe_id=1).order_by('-id')
    filter = Powers_character.objects.select_related('characters')
    return render(request, 'marvel/pageMarvel.html',
                  {'characterMarvel': list, 'filter': filter})


def listDC(request):
    list = Character.objects.filter(universe_id=2).order_by('-id')
    filter = Powers_character.objects.select_related('characters')
    return render(request, 'dc/pageDC.html', {'characterDC': list, 'filter': filter})


def listCharacters(request):
    filter = Powers_character.objects.select_related('characters')
    marvel = Character.objects.filter(universe_id=1).order_by('-id')
    dc = Character.objects.filter(universe_id=2).order_by('-id')
    return render(request, 'pages2/listCharacters.html', {'list': filter, 'marvel': marvel, 'dc': dc})

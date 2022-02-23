from django.shortcuts import render


def pageMain(request):
    return render(request, 'index.html')

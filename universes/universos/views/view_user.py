from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from universos.models import Character
from django.shortcuts import render, redirect

from universos.models import *


def loginUser(request):
    if request.method == 'POST':

        _usr = request.POST['user']
        _password = request.POST['pwd']

        user = authenticate(request, username=_usr, password=_password)

        print(user)
        if user:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'users/login.html', {'error': '[!]Usuario o contraseña incorrecta'})

    return render(request, 'users/login.html', {'user': loginUser})


@login_required
def logoutUser(request):
    logout(request)
    return render(request,'index.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from universos.models import *

from universos.form import CharacterForm
from universos.form import UpdateForm
from universos.form import Powers_character as Powers_character_form
from universos.form import PowersCreate as Power_form
from universos.form import PowerUpdate

from django.contrib import messages

import os.path
import re


def searchCharacter(request):
    letra = request.POST.get('letter', False)
    upper = str(letra).upper()
    print(letra)
    filter = Character.objects.filter(name__startswith=letra)

    return render(request, 'pages2/searchCharacter.html', {'found': filter, 'letra': letra})


def count(request):
    filter = Character.objects.filter(universe_id=1).count()
    filterDC = Character.objects.filter(universe_id=2).count()
    return render(request, 'pages2/countUniverses.html', {'count': filter, 'countDC': filterDC})


'''Guardar personaje usando lib form'''


@login_required
def save(request):
    form = CharacterForm(request.POST or None)
    ''' archivos = []
      archivos.append(form.image)
      for archivo in archivos:
          extension = os.path.splitext(archivo)
          patron = re.compile(r'/b.png')'''

    if form.is_valid():
        form.save()
        messages.success(request, 'Todo ha salido bien!!')
        return redirect('charactersMarvel')
    context = {
        'form': form,
    }
    return render(request, 'forms/form_save.html', context)


@login_required
def saveDC(request):
    form = CharacterForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Todo ha salido bien!!')
        return redirect('charactersDC')
    context = {
        'form': form,
    }
    return render(request, 'forms/form_save_Dc.html', context)


@login_required
def delete(request, id):
    get = Character.objects.get(id=id)
    get.delete()
    messages.success(request, 'Todo bien')
    return redirect('charactersMarvel')


@login_required
def deleteDC(request, id):
    get = Character.objects.get(id=id)
    get.delete()
    messages.success(request, 'Todo bien')
    return redirect('charactersDC')


@login_required
def update(request, id):
    obj = Character.objects.get(id=id)
    form = UpdateForm(request.POST or None, instance=obj)
    formP = Powers_character_form(request.POST or None)

    if form.is_valid() and formP.is_valid():
        form.save()
        formP.save()
        messages.success(request, 'Todo bien')
        return redirect('detail', obj.id)

    context = {
        'form': form,
        'form2': formP,
        'char': obj
    }
    return render(request, 'forms/form_update.html', context)


@login_required
def detail(request, id):
    obj = Character.objects.get(id=id)
    filt = Powers_character.objects.select_related('characters')
    context = {
        'char': obj,
        'filter': filt
    }
    return render(request, 'pages2/detail.html', context)

@login_required
def detaildc(request, id):
    obj = Character.objects.get(id=id)
    filt = Powers_character.objects.select_related('characters')
    context = {
        'char': obj,
        'filter': filt
    }
    return render(request, 'pages2/detaildc.html', context)


@login_required
# asignare poderes
def savePower(request):
    form = Powers_character_form(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Todo ha salido bien!!')
        return redirect('charactersMarvel')
    context = {
        'form': form

    }
    return render(request, 'forms/form_powers.html', context)


def savePowerDC(request):
    form = Powers_character_form(request.POST or None)
    lists = Character.objects.filter(universe_id=2)
    if form.is_valid():
        form.save()
        messages.success(request, 'Todo ha salido bien!!')
        return redirect('charactersDC')
    context = {
        'form': form,
        'character ': lists

    }
    return render(request, 'forms/form_powers_dc.html', context)


@login_required
# Crear poder
def createPower(request):
    form = Power_form(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'El per')
        return redirect('main')
    context = {
        'form': form

    }
    return render(request, 'forms/form_create_powers.html', context)


@login_required
# Eliminar poder del personaje
def deletePowerCharacter(request, id):
    powerObj = get_object_or_404(Powers_character, id=id)
    powerObj.delete()
    print(id)
    messages.success(request, 'epaa por fin')
    return redirect('charactersMarvel')


def deletePowerCharacterDC(request, id):
    powerObj = get_object_or_404(Powers_character, id=id)
    powerObj.delete()
    print(id)
    messages.success(request, 'epaa por fin')
    return redirect('charactersDC')


@login_required
# Actualizar poder
def updatePowerCharacter(request, id):
    obj = Powers.objects.get(id=id)
    form = PowerUpdate(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'epaa por fin')
        return redirect('deleteP')

    context = {
        'form': form,
        'char': obj
    }
    return render(request, 'forms/form_updatePower.html', context)


@login_required
# pagina de poderes
def pageDelete(request):
    get = Powers.objects.all()
    return render(request, 'powers/delete.html', {'powers': get})


# elimina poder completo
@login_required
def deletePower(request, id):
    get = Powers.objects.get(id=id)
    get.delete()
    messages.success(request, 'Todo bien')
    return redirect('deleteP')

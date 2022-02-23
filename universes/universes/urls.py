"""universes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from universos.views import views_characters as character_view

from universos.views import views_main as main_view
from universos.views import views_methods as methods_view
from universos.views import view_user as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view.pageMain, name='main'),

    path('characters/charactersMarvel/', character_view.listMarvel, name='charactersMarvel'),
    path('characters/charactersDC/', character_view.listDC, name='charactersDC'),

    path('characters/create-marvel/', methods_view.save, name='saveCharacter'),
    path('characters/create-dc/', methods_view.saveDC, name='saveCharacterDc'),

    path('characters/create/powers-marvel', methods_view.savePower, name='savePower'),
    path('characters/create/powers-dc', methods_view.savePowerDC, name='savePowerDC'),

    path('characters/create/create-powers', methods_view.createPower, name='createPower'),

    path('delete/<int:id>', methods_view.delete, name='delete'),
    path('delete-dc/<int:id>', methods_view.deleteDC, name='deleteDC'),

    path('characters/update/<int:id>', methods_view.update, name='update'),
    path('characters/detail/<int:id>', methods_view.detail, name='detail'),
    path('characters/detail-dc/<int:id>', methods_view.detaildc, name='detaildc'),

    path('totalCharacters/', methods_view.count, name='count'),

    path('searchCharacters/', methods_view.searchCharacter, name='search'),

    path('listCharacters/', character_view.listCharacters, name='list'),

    path('login/', user_view.loginUser, name='login'),
    path('logout/', user_view.logoutUser, name='logout'),

    path('delete-power-character-marvel/<int:id>', methods_view.deletePowerCharacter, name='deletePowerCharacter'),
    path('delete-power-character-dc/<int:id>', methods_view.deletePowerCharacterDC, name='deletePowerCharacterDc'),

    path('update-power/<int:id>', methods_view.updatePowerCharacter, name='updatePower'),

    path('info-Power/', methods_view.pageDelete, name='deleteP'),
    path('delete-power/<int:id>', methods_view.deletePower, name='deletePower')

]

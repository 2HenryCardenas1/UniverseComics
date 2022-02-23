from django import forms
from universos.models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        ordering = ['id']
        fields = [
            'name',
            'description',
            'image',
            'universe',
        ]
        labels = {
            'name': 'Nombre',
            'description': 'Descripcion',
            'image': 'Imagen',
            'universe': 'Universo'

        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'description': forms.Textarea(attrs={'placeholder': 'Escriba una pequeña descripcion',
                                                 'cols': 27, 'rows': 5, 'maxlenght': 250, 'text-aling': 'center'}),
            'image': forms.TextInput(
                attrs={'placeholder': 'Ingrese la imagen', 'required ': False, 'value': '/static/img/no-photo.png'})

        }

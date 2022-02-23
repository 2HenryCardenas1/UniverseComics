from django import forms
from django.db import migrations, models

from universos.models import Character


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name',
            'description',
            'image',
            'universe',
        ]

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Escriba una pequeña descripcion',
                                                 'cols': 27, 'rows': 5}),
            'image': forms.TextInput(attrs={'placeholder': 'Ingrese la imagen', 'value': ''})
        }

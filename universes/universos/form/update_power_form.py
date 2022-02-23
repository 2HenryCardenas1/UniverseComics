from django import forms
from django.db import migrations, models

from universos.models import Powers


class PowerUpdate(forms.ModelForm):
    class Meta:
        model = Powers
        ordering = ['id']
        fields = [
            'name'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Escriba el nombre del poder'}),
        }

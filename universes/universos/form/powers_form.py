
from django import forms
from universos.models import Powers_character



class Powers_character(forms.ModelForm):
    class Meta:
        model = Powers_character
        ordering = ['id']
        fields = [
            'characters',
            'powers',

            'number'
        ]
        labels = {
            'powers': 'Poder',
            'characters': 'Personaje',
            'number': 'Cantidad de poder'

        }






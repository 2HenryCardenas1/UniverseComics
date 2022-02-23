from django import forms
from universos.models import Powers

class PowersCreate(forms.ModelForm):
    class Meta:
        model = Powers
        ordering = ['id']
        fields = [
            'name'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Escriba el nombre del poder'}),
        }

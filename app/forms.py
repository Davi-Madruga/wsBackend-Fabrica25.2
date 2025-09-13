from django import forms
from .models import Pokemon,Ataque

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nome']
        widgets = {
            'nome' : forms.TextInput()
        }
        labels = {
            'nome' : 'Nome'
        }
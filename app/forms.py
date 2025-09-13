from django import forms
from .models import Pokemon,Ataque

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nome']
        widgets = {
            'nome' : forms.TextInput(),
        }
        labels = {
            'nome' : 'Nome',
        }

class AtaqueForm(forms.ModelForm):
    class Meta:
        model = Ataque
        fields = ['pokemon','nome']
        widgets = {
            'pokemon' : forms.Select(),
            'nome' : forms.TextInput(),
        }
        labels = {
            'pokemon' : 'Pokemon',
            'nome' : 'Nome',
        }
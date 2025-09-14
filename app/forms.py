from django import forms
from .models import Pokemon,Ataque

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nome']
        widgets = {
            'nome' : forms.TextInput(attrs={'placeholder':'Nome ou número'}),
        }
        labels = {
            'nome' : 'Nome',
        }

class AtaqueForm(forms.ModelForm):
    pokemon = forms.ModelChoiceField(
        queryset=Pokemon.objects.all(),           
        widget=forms.Select(),  
        label="Pokémon",
    )
    class Meta:
        model = Ataque
        fields = ['pokemon','nome']
        widgets = {

            'nome' : forms.TextInput(attrs={'placeholder':'Nome ou número'}),
        }
        labels = {
            'nome' : 'Nome',
        }
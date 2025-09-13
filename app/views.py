from django.shortcuts import render
from .models import Pokemon,Ataque

def listar_pokemons(request):
    pokemons = Pokemon.objects.all().order_by('id_pokemon')
    return render(request, 'listar_pokemons.html',{'pokemons':pokemons})

def procurar_pokemon(request):
    pass

def criar_pokemon(request):
    pass

def atualizar_pokemon(request):
    pass

def procurar_troca(request):
    pass

def deletar_pokemon(request):
    pass
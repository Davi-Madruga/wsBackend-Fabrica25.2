from django.shortcuts import render,redirect
from .models import Pokemon,Ataque
from .forms import PokemonForm
from .pokeapi import get_pokemon,get_ataque

def listar_pokemons(request):
    pokemons = Pokemon.objects.all().order_by('id_pokemon')
    return render(request, 'listar_pokemons.html',{'pokemons':pokemons})

def procurar_pokemon(request):
    form = PokemonForm()
    return render(request,'procurar_pokemon.html',{'form':form})

def criar_pokemon(request):
    if request.method == 'POST':
        pokemon = Pokemon()
        pokemon.id_pokemon = request.POST.get('id_pokemon')
        pokemon.nome = request.POST.get('nome')
        pokemon.tipos = request.POST.get('tipos')
        pokemon.altura = request.POST.get('altura')
        pokemon.peso = request.POST.get('peso')
        pokemon.save()
        return redirect('listar_pokemons')
    else:
        form = PokemonForm(request.GET)
        if form.is_valid():
            pokemon_name = form.cleaned_data['nome']
            pokemon_info = get_pokemon(pokemon_name)
            if pokemon_info:
                pokemon = Pokemon()
                pokemon.id_pokemon = pokemon_info['id']
                pokemon.nome = pokemon_info['name']
                tipos = '|'
                for t in pokemon_info['types']:
                    tipos += f"{t['type']['name']}|"
                pokemon.tipos = tipos
                pokemon.altura = pokemon_info['height']
                pokemon.peso = pokemon_info['weight']
                return render(request,'criar_pokemon.html',{'pokemon':pokemon})
            return render(request,'procurar_pokemon.html',{'form':form})   
         
def procurar_troca(request,pk):
    pass

def atualizar_pokemon(request,pk):
    pass

def deletar_pokemon(request,pk):
    pokemon = Pokemon.objects.get(pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('listar_pokemons')
    else:
        return render(request,'deletar_pokemon.html',{'pokemon':pokemon})
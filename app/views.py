from django.shortcuts import render,redirect
from .models import Pokemon,Ataque
from .forms import PokemonForm
from .pokeapi import get_pokemon,get_ataque

#POKEMONS

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
    pokemon_atual = Pokemon.objects.get(pk=pk)
    form = PokemonForm(instance=pokemon_atual)
    return render(request,'procurar_troca.html',{'pokemon_atual':pokemon_atual,'form':form})

def atualizar_pokemon(request,pk):
    pokemon_atual = Pokemon.objects.get(pk=pk)
    if request.method == 'POST':
        pokemon_atual.id_pokemon = request.POST.get('id_pokemon')
        pokemon_atual.nome = request.POST.get('nome')
        pokemon_atual.tipos = request.POST.get('tipos')
        pokemon_atual.altura = request.POST.get('altura')
        pokemon_atual.peso = request.POST.get('peso')
        pokemon_atual.save()
        return redirect('listar_pokemons')
    else:
        pokemon_atual.id_pokemon = request.GET.get('id_pokemon')
        pokemon_atual.nome = request.GET.get('nome_pokemon')
        pokemon_atual.tipos = request.GET.get('tipos')
        pokemon_atual.altura = request.GET.get('altura')
        pokemon_atual.peso = request.GET.get('peso')
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
                return render(request,'atualizar_pokemon.html',{'pokemon':pokemon,'pokemon_atual':pokemon_atual})            
            return render(request,'procurar_troca.html',{'pokemon_atual':pokemon_atual,'form':form})
        else:
            return render(request,'procurar_troca.html',{'pokemon_atual':pokemon_atual,'form':form})

def deletar_pokemon(request,pk):
    pokemon = Pokemon.objects.get(pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('listar_pokemons')
    else:
        return render(request,'deletar_pokemon.html',{'pokemon':pokemon})
    
#ATAQUES

def listar_ataques(request):
    ataques = Ataque.objects.all()
    return render(request,'zlistar_ataques.html',{'ataques':ataques})

def procurar_ataque(request):
    pass

def criar_ataque(request):
    pass

def procurar_troca_ataque(request,pk):
    pass

def trocar_ataque(request,pk):
    pass

def deletar_ataque(request,pk):
    pass
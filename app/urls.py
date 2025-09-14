from django.urls import path
from . import views

urlpatterns = [
    #POKEMONS
    path('',views.listar_pokemons,name='listar_pokemons'),
    path('procurar_pokemon/',views.procurar_pokemon,name='procurar_pokemon'),
    path('criar_pokemon/',views.criar_pokemon,name='criar_pokemon'),
    path('procurar_troca/<int:pk>/',views.procurar_troca,name='procurar_troca'),
    path('atualizar_pokemon/<int:pk>/',views.atualizar_pokemon,name='atualizar_pokemon'),
    path('deletar_pokemon/<int:pk>/',views.deletar_pokemon,name='deletar_pokemon'),
    path('detalhar_pokemon/<int:pk>/',views.detalhar_pokemon,name='detalhar_pokemon'),
    #ATAQUES    
    path('listar_ataques/',views.listar_ataques,name='listar_ataques'),
    path('procurar_ataque/',views.procurar_ataque,name='procurar_ataque'),
    path('criar_ataque/',views.criar_ataque,name='criar_ataque'),
    path('atualizar_ataque/<int:pk>/',views.atualizar_ataque,name='atualizar_ataque'),
    path('deletar_ataque/<int:pk>/',views.deletar_ataque,name='deletar_ataque'),
]
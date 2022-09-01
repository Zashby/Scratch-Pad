from django.urls import path
from . import views

app_name = 'pokeapp'

urlpatterns =[ 
    path('', views.index, name='index'),

    path('api/pokemonlist', views.pokemon_list, name='pokemon_list'),

    path('pokecheck/<int:pokemon_number>', views.pokecheck , name='pokecheck' ),

    path('api/pokesearch/<str:search_term>', views.pokesearch, name='pokesearch'),

    
]
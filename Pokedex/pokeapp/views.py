from unicodedata import name
from django.shortcuts import render, redirect
from .models import Pokemon, manyTypes
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'pokeapp/index.html')


def pokemon_list(request):
    pokemon = Pokemon.objects.all()
    pokemon_api = []
    for pokemon in pokemon:
        pokemon_api.append({
            'number' : pokemon.number,
            'name': pokemon.name,
            'height': pokemon.height,
            'weight': pokemon.weight,
            'types': pokemon.types,
            'image_front': pokemon.image_front,
            'image_back': pokemon.image_back,
            # how to return ManytoMany queryset
            'many_types': list(pokemon.many_types.all().values()),

        })
    return JsonResponse(list(pokemon_api), safe=False)

def pokecheck(request, pokemon_number):
    try:
        pokemon = Pokemon.objects.get(number=pokemon_number)
        types = list(pokemon.many_types.all().values())
        context = {
            'pokemon': pokemon,
            'types': types
        }
        print(context)
        return render(request, 'pokeapp/pokepage.html', context)
    except Pokemon.DoesNotExist:
        pass
    return redirect('pokeapp:index')

def pokesearch(request, search_term):
    pokemon_api= []
    if request.method == 'GET':
        pokemon = Pokemon.objects.filter(Q(types__icontains=search_term) | Q(name__icontains=search_term) | Q(number__icontains=search_term))
        for poke in pokemon:
            pokemon_api.append({
            'number' : poke.number,
            'name': poke.name,
            'height': poke.height,
            'weight': poke.weight,
            'types': poke.types,
            'image_front': poke.image_front,
            'image_back': poke.image_back,
            # how to return ManytoMany queryset
            'many_types': list(poke.many_types.all().values()),

        })
        return JsonResponse(list(pokemon_api), safe=False)
    
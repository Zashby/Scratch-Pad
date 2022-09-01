from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon, manyTypes
import json




class Command(BaseCommand):
    
        def handle(self, *args, **kwargs):
                Pokemon.objects.all().delete()
                manyTypes.objects.all().delete()
                with open('pokemon.json','r') as f:
                        response = f.read()
                        pokemon_list = json.loads(response)
                        for pokemon in pokemon_list['pokemon']:
                                # print(pokemon['number'],)
                                # print    (pokemon['name'],)
                                # print    (pokemon['height'],)
                                # print   (pokemon['weight'],)
                                # print    (pokemon['image_front'],)
                                # print    (pokemon['image_back'],)
                                # print   (', '.join(pokemon['types']))
                                current_pokemon = Pokemon.objects.create(
                                        number = pokemon['number'],
                                        name = pokemon['name'],
                                        height = round(int(pokemon['height']/10)),
                                        weight = round(int(pokemon['weight']/10)),
                                        image_front = pokemon['image_front'],
                                        image_back = pokemon['image_back'],
                                        types = ', '.join(pokemon['types']),        
                                )
                                for type in pokemon['types']:
                                        
                                        try:
                                                current_type = manyTypes.objects.get(name = type)
                                                
                                        except manyTypes.DoesNotExist:
                                                
                                                current_type = manyTypes.objects.create(name = type)
                                                
                                        current_pokemon.many_types.add(current_type)                               
                                        current_pokemon.save()


#     number = models.IntegerField()
#     name = models.CharField(max_length=30)
#     height = models.FloatField()
#     weight = models.FloatField()
#     image_front = models.CharField(max_length=150)
#     image_back = models.CharField(max_length=150)
#     types = models.CharField(max_length=50)
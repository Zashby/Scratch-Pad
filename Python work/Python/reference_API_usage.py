import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")

print(response.text)

pokedex = (response.json())

print(len(pokedex))

pokemon = pokedex["results"]

print(len(pokemon))

for i, poke in enumerate    (pokemon):
    print(f"No {i+1}\t{poke['name']}")
    if poke["name"]== "bulbasaur":
        print(poke)
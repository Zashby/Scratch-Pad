
from django.shortcuts import render
from django.http import HttpResponse
import string
# Create your views here.
def index(request):


    message = request.POST.get('message', "")
    rotation = int(request.POST.get('rotations', 0))
    encoded = ""
    characters = [string.ascii_lowercase, string.ascii_uppercase,string.digits," ", string.punctuation]
       
    for letter in message:
            for char in characters:
                if letter in char:
                    location = char.index(letter)
                    encoded += char[(location + rotation) % len(char)]
    context = { 'encoded': encoded
        }


    return render(request, 'rot/index.html', context)


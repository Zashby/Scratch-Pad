from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Person, State
from .forms import UpdatePersonForm
def index(request):

    if request.method == 'POST':
        print(request.POST) # remove prior to release (For Testing Purposes)
        person = Person()
        person.first_name = request.POST.get('first_name')
        person.last_name = request.POST.get('last_name')
        person.age = request.POST.get('age')
        
        state_id = int(request.POST.get('state'))
        state = State.objects.get(id = state_id)
        person.state = state
       
        if request.POST.get('besties'):
            person.is_close_friend = True
        print(request.POST)
        person.save()
    people= Person.objects.all()
    states = State.objects.all()
    context = {'people':people, 'states':states}
    
    return render(request, 'people/index.html', context )

def person_detail(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        #Reverse can look up redirect by "name"
        return HttpResponseRedirect(reverse('index'))
    
    formData = {
        'first_name': person.first_name,    
        'last_name': person.last_name,
        'age': person.age,
        'besties': person.is_close_friend, 
    }

    context = {
        'person': person, 
        "form":UpdatePersonForm(formData),
        }

    return render(request, 'people/detail.html', context)
# Create your views here.

# update person
def update(request, person_id):
    print(request.POST)
    
    form = UpdatePersonForm(request.POST)
    if form.is_valid():
        person = Person.objects.get(id=person_id)
        person.first_name = form.cleaned_data['first_name']
        person.last_name = form.cleaned_data['last_name']
        person.age = form.cleaned_data['age']
        if form.cleaned_data['besties']:
            person.is_close_friend = True
        else:
            person.is_close_friend = False

        person.save()

    return HttpResponseRedirect(reverse('person_details', args=(person_id,)))


# Delete stuff
def delete(requests, person_id):
    person = Person.objects.get(id=person_id)
    
    
    person.delete()
    
    
    return HttpResponseRedirect(reverse('index'))
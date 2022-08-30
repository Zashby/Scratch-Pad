from itertools import filterfalse
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import User, Group
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, 'mapr_app/index.html')

# method of getting data translated into JSON format
# def get_users(request):
#     context = {}
#     users = User.objects.filter(restricted=False, private=False).values_list('username', 'location__longitude', 'location__latitude', 'groups__name')
#     return JsonResponse(list(users), safe=False)

def get_users_public(request):
    users_query = User.objects.filter(restricted=False, private=False)[:50]

    users = []
    for user in users_query:
        users.append({
            'username': user.username,
            'location': {
                'longitude': user.location.longitude,
                'latitude': user.location.latitude
            },
            'groups':list(user.groups.filter(private=False).values( 'id', 'name'))
            
        })
    return JsonResponse(list(users), safe=False)

def get_groups(request):
    groups = list(Group.objects.filter(private=False).values())
    return JsonResponse({'data':groups})



def get_group_id(request, group_id):
    group = Group.objects.get(id=group_id)
    users = list(group.users.filter(restricted=False, private=False).all().values('location__longitude', 'location__latitude', 'username'))
    return JsonResponse({'data':users})
    

def login(request):
    if request.method == 'GET':
        return render(request, 'mapr_app/login.html')
    elif request.method == 'POST':

    
        data = json.loads(request.body)
        username = data.get['username', '']
        password = data.get['password', '']
        print(username, password)
        user = auth.authenticate(request, username=username, password=password)
        if user== None:
            return JsonResponse({'Message':"Invalid username or password"})
        else:
            auth.login(request, user)
            return JsonResponse({'message':'ok'})


def get_test_groups(request):
    print(request.user)
    groups=list(Group.objects.filter(users__username=request.user.username))

def vue_index(request):
    return render(request, 'mapr_app/vue.html')
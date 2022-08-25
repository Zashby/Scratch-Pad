from itertools import filterfalse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User, Group

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
    
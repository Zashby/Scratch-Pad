from django.core.management.base import BaseCommand

from mapr_app.models import User, Location, Group

import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        

        # Delete old test database users sans admin user
        print('Clearing database')
        Group.objects.all().delete()
        Location.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()
        print('Database cleared... repopulating')


        print('Creating test users')
        groups=[]
        for x in range(10):
            if x%2==0:
                group = Group()
                group.name= f'testgroup{x}'
                group.save()
                groups.append(group)
            else:
                group = Group()
                group.name= f'testgroup{x}'
                group.private=False
                group.save()
                groups.append(group)



        for x in range(200):
            print(f'creating test user {x}')
            location = Location()
            location.latitude = round(random.randrange(-9000000,9000000)/100000, 5)
            location.longitude = round(random.randrange(-18000000,18000000)/100000, 5)
            location.save()
            u = User.objects.create_user(
                    username=f'user{x}',
                    password='pass',
                    private = False,
                    location= location)
            u.groups.add(random.choice(groups))
            if x%random.randint(1,10)==0:
                u.private = True
                print(f'created user {x} is private')
                u.groups.add(random.choice(groups))
            elif x%3==0:
                u.restricted = True
                print(f'created user {x} is restricted')
            u.save()

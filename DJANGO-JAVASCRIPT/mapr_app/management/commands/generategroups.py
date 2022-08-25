from django.core.management.base import BaseCommand
import random
from mapr_app.models import User, Group

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Group.objects.all().delete()
        users = User.objects.all()
        groups =[]
        for x in range(3):
            group = Group()
            group.name=f'testgroup{x}'
            group.save()
            groups.append(group)
            print(f'generated group {x}')
        for user in users:
        
            group =random.choice(groups)
            print(f'{user.username} added to {group.name}')
            user.groups.add(group)
            user.save()
from django.core.management.base import BaseCommand

from mapr_app.models import User
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.filter(is_superuser=False).delete()
        for x in range(20):
            if x%random.randint(1,9)==0:
                u = User.objects.create_user(
                    username=f'user{x}',
                    password='pass',
                    
                )
                print(f'created user {x} private')

            else:
                u = User.objects.create_user(
                    username=f'user{x}',
                    password='pass',
                    private=False,
                )
                print(f'created user {x} public')
            
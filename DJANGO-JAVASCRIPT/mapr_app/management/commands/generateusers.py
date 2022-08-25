from django.core.management.base import BaseCommand

from mapr_app.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.filter(is_superuser=False).delete()
        for x in range(0,10):
            u = User.objects.create_user(
                username=f'user{x}',
                password='pass'
            )
            print(f'created user {x}')
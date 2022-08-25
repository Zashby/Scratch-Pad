from django.core.management.base import BaseCommand
import random
from mapr_app.models import User, Group

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Group.objects.filter(user_set__is_null=True).delete()
        users = User.objects.all()
        groups =[]
        for x in range(3):
            group = Group()
            group.name=f'testgroup{x}'
            group.save()
            groups.append(group)

        for user in users:
            group =random.choice(groups)
            user.groups.add(group)
            user.save()
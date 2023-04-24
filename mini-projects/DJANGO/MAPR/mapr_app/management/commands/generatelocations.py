from django.core.management.base import BaseCommand
import random

from mapr_app.models import Location, User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Location.objects.all().delete()
        users = User.objects.all()
        
        for user in users:
            if user.location:
                continue
            location = Location()
            latitude = round(random.randrange(-9000000,9000000)/100000, 5)
            longitude = round(random.randrange(-18000000,18000000)/100000, 5)
            
            location.longitude = longitude
            location.latitude = latitude
            print(latitude, longitude)
            location.save()

            user.location = location
            user.save()
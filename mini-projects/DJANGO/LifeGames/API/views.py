from rest_framework.response import Response
from rest_framework.decorators import api_view
import MealDeck.models


@api_view(['GET'])
def TestData(request):
    TestUser = {'name': 'Bobson', 'age' : 25, 'sex': 'yes',}

    return Response(TestUser)
from django.urls import path
from . import views

app_name='MealDeck'

urlpatterns = [
    path('', views.index, name='index')
]

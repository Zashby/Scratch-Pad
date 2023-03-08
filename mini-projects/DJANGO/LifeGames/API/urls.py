from django.urls import path
from . import views

urlpatterns = [
    path('whatever/', views.TestData),
]

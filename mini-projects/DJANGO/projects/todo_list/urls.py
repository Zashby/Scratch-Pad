from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('delete/<int:index>/', views.delete_todo),

    path("complete/<int:index>/", views.complete_todo),
    
]

from django.urls import path
from . import views


urlpatterns = [
   path('', views.index),

   path('vue/', views.vue_index, name='vue_index'),

   path('login/', views.login, name='login'),

   path('api/userspublic/', views.get_users_public, name='get_users_public'),

   path('api/groups/', views.get_groups, name='get_groups'),

   path('api/groups/<int:group_id>', views.get_group_id, name='get_group_id'),


   
]

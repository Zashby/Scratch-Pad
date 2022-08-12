from django.urls import path
from . import views


app_name = 'todo'


urlpatterns = [
    path('', views.index, name='index'),

    path('signup/', views.signup, name='signup'),

    path('login/', views.login, name='login'),

    path('logout/', views.logout, name='logout'),

    path('create/', views.create, name='create'),
    
    path('delete/<int:todo_id>', views.delete, name='delete'),

    path('update/<int:todo_id>', views.update, name='update'),

    path('complete/<int:todo_id>', views.complete, name='complete'),
]

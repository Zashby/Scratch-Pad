from django.urls import path
from . import views

urlpatterns = [ 

    path('', views.index, name='index'),

    path('detail/<int:person_id>/', views.person_detail, name='person_details'),

    path('update/<int:person_id>/', views.update, name='update'),

    path('delete/<int:person_id>', views.delete, name='delete'),
]
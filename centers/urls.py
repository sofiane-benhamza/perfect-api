from django.urls import path
from . import views

urlpatterns = [
     path('create/', views.center_create, name='create'),
     path('read/', views.center_read, name='read'),
     path('update/', views.center_update, name='update'),
     path('delete/', views.center_delete, name='delete'),
]


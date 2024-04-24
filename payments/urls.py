from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.payment_create, name='create'),
    path('read/', views.payment_read, name='read'),
    path('update/', views.payment_update, name='update'),
    path('delete/', views.payment_delete, name='delete'),
]


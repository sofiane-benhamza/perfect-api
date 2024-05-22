from django.urls import path, include
from .views import users_view

urlpatterns = [
        path('', users_view, name='users'),    
]


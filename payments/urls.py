from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payments_views, name="centre"),

]


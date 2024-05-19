from django.urls import path
from . import views

urlpatterns = [
    path('centre/', views.centers_view, name="centre"),

]


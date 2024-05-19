from django.urls import path
from . import views

urlpatterns = [
    path('diploma/', views.diploma_view, name="diploma"),

    path('experience/', views.experience_view, name="experience"),

    path('professors/', views.professors_view, name="professors"),

     path('review/', views.review_view, name="review"),

     path('students/', views.students_view ,name="students"),
]
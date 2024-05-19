from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses_view, name="courses"),

    path('review_course/', views.review_course_view, name="review_course"),

    path('completed_courses/', views.completed_courses_view, name="completed_courses"),

     path('certificate/', views.certificate_view, name="certificate"),

     path('quiz/', views.quiz_view ,name="quiz"),
]
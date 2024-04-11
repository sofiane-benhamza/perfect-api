from django.contrib import admin
from django.urls import path, include 

import centers
import courses
import payments
import authentication

urlpatterns = [
    path('users/', include('authentication.urls')),
    path('centers/', include('centers.urls')),
    path('courses/', include('courses.urls')),
    path('payments/', include('payments.urls')),
]

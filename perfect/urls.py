from django.contrib import admin
from django.urls import path, include 

import authentication
import centers.urls
import courses
import payments

urlpatterns = [
    path('users/', include('authentication.urls')),
    path('centers/', include('centers.urls')),
    path('courses/', include('courses.urls')),
    path('payments/', include('payments.urls')),
]

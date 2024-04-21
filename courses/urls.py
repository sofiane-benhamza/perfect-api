from django.urls import path, include
from .courses import course_create, course_delete, course_read, course_update
from .ReviewsCourse import reviews_course_create,reviews_course_read,reviews_course_update,reviews_course_delete
from .CompletedCourses import completed_courses_create,completed_courses_delete,completed_courses_read,completed_courses_update
from .Certificate import certificate_create,certificate_delete,certificate_read,certificate_update
from.Quiz import quiz_create,quiz_delete,quiz_read,quiz_update
urlpatterns = [
    path('Courses/', include([
        path('create/', course_create, name='course_create'),
        path('read/', course_read, name='course_read'),
        path('update/', course_update, name='course_update'),
        path('delete/', course_delete, name='course_delete'),
    ])),

    path('ReviewsCourse/', include([
        path('create/', reviews_course_create, name='reviews_course_create'),
        path('read/', reviews_course_read, name='reviews_course_read'),
        path('update/', reviews_course_update, name='reviews_course_update'),
        path('delete/', reviews_course_delete, name='reviews_course_delete'),
    ])),

    path('CompletedCourses/', include([
         path('create/', completed_courses_create, name='completed_courses_create'),
         path('read/', completed_courses_read, name='completed_courses_read'),
         path('update/', completed_courses_update, name='completed_courses_update'),
         path('delete/', completed_courses_delete, name='completed_courses_delete'),
    ])),

     path('Certificate/', include([
         path('create/', certificate_create, name='certificate_create'),
         path('read/', certificate_read, name='certificate_read'),
         path('update/', certificate_update, name='certificate_update'),
         path('delete/', certificate_delete, name='certificate_delete'),
     ])),

     path('Quiz/', include([
         path('create/', quiz_create, name='quiz_create'),
         path('read/', quiz_read, name='quiz_read'),
         path('update/', quiz_update, name='quiz_update'),
         path('delete/', quiz_delete, name='quiz_delete'),
     ])),
]

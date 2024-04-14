from django.urls import path, include

from .students import student_create, student_read, student_update, student_delete
from .professors import professor_create, professor_read, professor_update, professor_delete
from .diploma import diploma_create, diploma_read, diploma_update, diploma_delete
from .review import review_create, review_read, review_update, review_delete
from .experience import experience_create, experience_read, experience_update, experience_delete

urlpatterns = [
    path('students/', include([
        path('create/', student_create, name='student_create'),
        path('read/', student_read, name='student_read'),
        path('update/', student_update, name='student_update'),
        path('delete/', student_delete, name='student_delete'),
    ])),
     path('professors/', include([
         path('create/', professor_create, name='professor_create'),
         path('read/', professor_read, name='professor_read'),
         path('update/', professor_update, name='professor_update'),
         path('delete/', professor_delete, name='professor_delete'),
     ])),
    
      path('diploma/', include([
          path('create/', diploma_create, name='diploma_create'),
          path('read/', diploma_read, name='diploma_read'),
          path('update/', diploma_update, name='diploma_update'),
          path('delete/', diploma_delete, name='diploma_delete'),
      ])),
     path('review/', include([
         path('create/', review_create, name='review_create'),
         path('read/', review_read, name='review_read'),
         path('update/', review_update, name='review_update'),
         path('delete/', review_delete, name='review_delete'),
     ])),
     path('experience/', include([
         path('create/', experience_create, name='experience_create'),
         path('read/', experience_read, name='experience_read'),
         path('update/', experience_update, name='experience_update'),
         path('delete/', experience_delete, name='experience_delete'),
     ])),
]


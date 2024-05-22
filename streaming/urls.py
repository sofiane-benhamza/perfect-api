from django.urls import path
from .views import stream_video, get_videos

urlpatterns = [
    path('names/', get_videos, name='get_videos'),
    path('videos/', stream_video, name='stream_video'),
    # other urlpatterns
]

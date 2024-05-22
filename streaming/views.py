from django.shortcuts import render
from django.http import FileResponse, HttpResponseNotFound, JsonResponse
from django.conf import settings
import os
import re
from rest_framework.decorators import api_view # type: ignore



def natural_sort(text):
    return [int(c) if c.isdigit() else c for c in re.split(r'(^\d+|\d+$)', text)]

@api_view(['GET'])
def get_videos(request):
    try:
        videos = os.listdir("videos/")

        # Sort videos alphanumerically
        videos.sort(key=natural_sort)


        return JsonResponse({"videos": videos}, status=200)

    except FileNotFoundError:
        return HttpResponseNotFound("Videos directory not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Log the error for troubleshooting
        return HttpResponseNotFound("Something went wrong.")  # Generic error message for user


@api_view(['GET'])
def stream_video(request):
    video_name = request.GET.get("video", "animals.mp4")
    permission = request.GET.get("permission")
    video_path = "videos/"+video_name
    if video_name.endswith(".mp4"):
        type="video/mp4"
    else:
        type="image/jpeg"

    if os.path.exists(video_path):
        return FileResponse(open(video_path, 'rb'), content_type=type)
    else:
        return HttpResponseNotFound("Video not found")





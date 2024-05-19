from django.urls import path
from . import views

from django.http import JsonResponse
from rest_framework.decorators import api_view # type: ignore
from .diploma import diploma_create,diploma_delete,diploma_read,diploma_update
from .experience import experience_create,experience_delete,experience_read,experience_update
from .professors import professor_create,professor_delete,professor_read,professor_update
from .review import review_create,review_delete,review_read,review_update
from .students import student_create,student_delete,student_read,student_update

@api_view(['POST', 'GET','PUT','DELETE'])
def diploma_view(request):
    method_switch = {
        "POST": diploma_create,
        "GET": diploma_read,
        "PUT": diploma_update,
        "DELETE": diploma_delete,

    }

    handler = method_switch.get(request.method)

    if handler:
        return handler(request)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=401)
    
@api_view(['POST', 'GET','PUT','DELETE'])
def experience_view(request):
    method_switch = {
        "POST": experience_create,
        "GET": experience_read,
        "PUT": experience_update,
        "DELETE": experience_delete,

    }

    handler = method_switch.get(request.method)

    if handler:
        return handler(request)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=401)
    
@api_view(['POST', 'GET','PUT','DELETE'])
def professors_view(request):
    method_switch = {
        "POST": professor_create,
        "GET": professor_read,
        "PUT": professor_update,
        "DELETE": professor_delete,

    }

    handler = method_switch.get(request.method)

    if handler:
        return handler(request)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=401)
    
@api_view(['POST', 'GET','PUT','DELETE'])
def review_view(request):
    method_switch = {
        "POST": review_create,
        "GET": review_read,
        "PUT": review_update,
        "DELETE": review_delete,

    }

    handler = method_switch.get(request.method)

    if handler:
        return handler(request)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=401)

@api_view(['POST', 'GET','PUT','DELETE'])
def students_view(request):
    method_switch = {
        "POST": student_create,
        "GET": student_read,
        "PUT": student_update,
        "DELETE": student_delete,

    }

    handler = method_switch.get(request.method)

    if handler:
        return handler(request)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=401)

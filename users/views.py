from django.http import JsonResponse
from django.shortcuts import render
from .students import create, read, update, disconnect, connect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def users_view(request):
    students_switch = {
            'POST': create,
            'GET': read,
            'PUT': update,
            'PATCH': connect,
            'DELETE': disconnect,
            }
    handler = students_switch.get(request.method)
    if handler:
        return handler(request)
    else:
        return JsonResponse({"error": "something went wrong"}, status=401)
    
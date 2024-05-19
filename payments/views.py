from django.http import JsonResponse
from .payments import payment_read,payment_create
from .models import Payments
from rest_framework.decorators import api_view

@api_view(['POST', 'GET','PUT','DELETE'])

def payments_view(request):
    method_switch = {
        "POST": payment_create,
        "GET": payment_read,
        

    }

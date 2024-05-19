from django.http import JsonResponse

from .centers import center_create, center_delete, center_read, center_update
from .models import Center
from rest_framework.decorators import api_view # type: ignore


@api_view(['POST', 'GET','PUT','DELETE'])
def centers_view(request):
    method_switch = {
        "POST": center_create,
        "GET": center_read,
        "PUT": center_update,
        "DELETE": center_delete,

    }

    handler = method_switch.get(request.method)

    if handler:
        return handler(request)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=401)

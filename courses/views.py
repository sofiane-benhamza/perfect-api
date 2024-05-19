from django.http import JsonResponse
from rest_framework.decorators import api_view # type: ignore
from .ReviewsCourse import reviews_course_create,reviews_course_delete,reviews_course_read,reviews_course_update
from .courses import course_create, course_read, course_update, course_delete
from .CompletedCourses import completed_courses_create, completed_courses_read, completed_courses_update, completed_courses_delete
from .Certificate import certificate_create, certificate_read, certificate_update, certificate_delete
from .Quiz import quiz_create, quiz_read, quiz_update, quiz_delete

@api_view(['POST', 'GET','PUT','DELETE'])
def courses_view(request):
    method_switch = {
        "POST": course_create,
        "GET": course_read,
        "PUT": course_update,
        "DELETE": course_delete,

    }

    handler = method_switch.get(request.method)

    if handler:
        return handler(request)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=401)
    
@api_view(['POST', 'GET','PUT','DELETE'])
def review_course_view(request):
    method_switch = {
        "POST": reviews_course_create,
        "GET": reviews_course_read,
        "PUT": reviews_course_update,
        "DELETE": reviews_course_delete,

    }

    handler = method_switch.get(request.method)

    if handler:
        return handler(request)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=401)
    
@api_view(['POST', 'GET','PUT','DELETE'])
def completed_courses_view(request):
    method_switch = {
        "POST": completed_courses_create,
        "GET": completed_courses_read,
        "PUT": completed_courses_update,
        "DELETE": completed_courses_delete,

    }

    handler = method_switch.get(request.method)

    if handler:
        return handler(request)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=401)
    
@api_view(['POST', 'GET','PUT','DELETE'])
def certificate_view(request):
    method_switch = {
        "POST": certificate_create,
        "GET": certificate_read,
        "PUT": certificate_update,
        "DELETE": certificate_delete,

    }

    handler = method_switch.get(request.method)

    if handler:
        return handler(request)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=401)

@api_view(['POST', 'GET','PUT','DELETE'])
def quiz_view(request):
    method_switch = {
        "POST": quiz_create,
        "GET": quiz_read,
        "PUT": quiz_update,
        "DELETE": quiz_delete,

    }

    handler = method_switch.get(request.method)

    if handler:
        return handler(request)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=401)
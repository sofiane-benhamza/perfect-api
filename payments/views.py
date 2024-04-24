from django.http import JsonResponse
from authentication.models import UserStudent
from courses.models import Courses
import payments
from .models import payment
from rest_framework.decorators import api_view


@api_view(["POST"])
def payment_create(request):
    if request.method == "POST":
        data = request.data
        date = data.get("date")

        course_name = data.get("course_name")
        course = Courses.objects.get(name=course_name)

        student_email = data.get(student_email)
        student = UserStudent.objects.get(email=student_email)

        if student and course and date:

            user_payment = payments.objects.create(
                date=date,
                course=course,
                student=student
            )
            return JsonResponse({"message": "payment created successfully"})
        else:
            return JsonResponse({"error": "Missing required fields"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@api_view(["GET"])
def payment_read(request):
    if request.method == "GET":
        data= request.GET
        course_name = data.get("course_name")
        course = Courses.objects.get(name=course_name)

        student_email = data.get(student_email)
        student = UserStudent.objects.get(email=student_email)
        if student and course:
            try:
                payment = payment.objects.get(student=student, course=course)
                serialized_payment = {
                    "date": payment.date,
                    "course": payment.course,
                }
                return JsonResponse({"payment": serialized_payment})
            except payment.DoesNotExist:
                return JsonResponse({"error": "payment not found"}, status=404)
        else:
            return JsonResponse({"error": "Email parameter is missing"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

# NO UPDATE , DELETE,=> noo need
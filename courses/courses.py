from django.http import JsonResponse
from .models import Courses
from rest_framework.decorators import api_view # type: ignore


@api_view(["POST"])
def course_create(request):
    if request.method == "POST":
        data = request.data
        name = data.get("name")
        speciality = data.get("speciality")
        price = data.get("price")
        review_number = data.get("review_number")
        review_score = data.get("review_score")

        if not (name and speciality and price and review_number and review_score):
            return JsonResponse({"error": "Missing required fields"}, status=400)

        course = Courses.objects.create(
            name=name,
            speciality=speciality,
            price=price,
            review_number=review_number,
            review_score=review_score
        )
        if course:
            return JsonResponse(
                {"message": "Course created successfully"}, status=200
            )
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@api_view(['GET'])
def course_read(request):
    if request.method == "GET":
        course_id = request.GET.get("id")
        if course_id is not None:
            try:
                course = Courses.objects.get(id=course_id)
                serialized_course = {
                    "name": course.name,
                    "speciality": course.speciality,
                    "price": course.price,
                    "review_number": course.review_number,
                    "review_score": course.review_score
                }
                return JsonResponse({"course": serialized_course})
            except Courses.DoesNotExist:
                return JsonResponse({"error": "Course not found"}, status=404)
        else:
            return JsonResponse({"error": "Course ID parameter is missing"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@api_view(['PUT'])
def course_update(request):
    if request.method == 'PUT':
        data = request.data
        course_id = data.get('id')
        try:
            course = Courses.objects.get(id=course_id)
            course.name = data.get('name')
            course.speciality = data.get('speciality')
            course.price = data.get('price')
            course.review_number = data.get('review_number')
            course.review_score = data.get('review_score')
            course.save()
            return JsonResponse({'message': 'Course updated successfully'})
        except Courses.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@api_view(['DELETE'])
def course_delete(request):
    if request.method == 'DELETE':
        data = request.data
        course_id = data.get('id')
        try:
            course = Courses.objects.get(id=course_id)
            course.delete()
            return JsonResponse({'message': 'Course deleted successfully'})
        except Courses.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

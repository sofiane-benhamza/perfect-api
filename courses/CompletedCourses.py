from django.http import JsonResponse
from .models import CompletedCourses
from rest_framework.decorators import api_view # type: ignore

@api_view(["POST"])
def completed_courses_create(request):
    if request.method == "POST":
        data = request.data
        start_date = data.get("start_date")
        finish_date = data.get("finish_date")
        user_student_id = data.get("user_student_id")
        course_id = data.get("course_id")

        if not (start_date and finish_date and user_student_id and course_id):
            return JsonResponse({"error": "Missing required fields"}, status=400)

        try:
            completed_course = CompletedCourses.objects.create(
                start_date=start_date,
                finish_date=finish_date,
                user_student_id=user_student_id,
                course_id=course_id
            )
            return JsonResponse(
                {"message": "Completed course created successfully"}, status=200
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['GET'])
def completed_courses_read(request):
    if request.method == "GET":
        course_id = request.GET.get("id")
        if course_id is not None:
            try:
                completed_course = CompletedCourses.objects.get(id=course_id)
                serialized_completed_course = {
                    "start_date": completed_course.start_date,
                    "finish_date": completed_course.finish_date,
                    "user_student_id": completed_course.user_student_id,
                    "course_id": completed_course.course_id,
                }
                return JsonResponse({"completed_course": serialized_completed_course})
            except CompletedCourses.DoesNotExist:
                return JsonResponse({"error": "Completed course not found"}, status=404)
        else:
            return JsonResponse({"error": "Completed course ID parameter is missing"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['PUT'])
def completed_courses_update(request):
    if request.method == 'PUT':
        data = request.data
        course_id = data.get('id')
        try:
            completed_course = CompletedCourses.objects.get(id=course_id)
            completed_course.start_date = data.get('start_date')
            completed_course.finish_date = data.get('finish_date')
            completed_course.user_student_id = data.get('user_student_id')
            completed_course.course_id = data.get('course_id')
            completed_course.save()
            return JsonResponse({'message': 'Completed course updated successfully'})
        except CompletedCourses.DoesNotExist:
            return JsonResponse({'error': 'Completed course not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['DELETE'])
def completed_courses_delete(request):
    if request.method == 'DELETE':
        data = request.data
        course_id = data.get('id')
        try:
            completed_course = CompletedCourses.objects.get(id=course_id)
            completed_course.delete()
            return JsonResponse({'message': 'Completed course deleted successfully'})
        except CompletedCourses.DoesNotExist:
            return JsonResponse({'error': 'Completed course not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

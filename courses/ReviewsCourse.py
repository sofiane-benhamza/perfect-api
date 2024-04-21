from django.http import JsonResponse
from .models import ReviewsCourse,Courses
from rest_framework.decorators import api_view # type: ignore

@api_view(["POST"])
def reviews_course_create(request):
    if request.method == "POST":
        data = request.data
        given_score = data.get("given_score")
        date = data.get("date")
        course_id = data.get("course_id")

        if not (given_score and date and course_id):
            return JsonResponse({"error": "Missing required fields"}, status=400)

        try:
            course = Courses.objects.get(id=course_id)
            review = ReviewsCourse.objects.create(
                given_score=given_score,
                date=date,
                course=course
            )
            return JsonResponse(
                {"message": "Review created successfully"}, status=200
            )
        except Courses.DoesNotExist:
            return JsonResponse({"error": "Course not found"}, status=404)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['GET'])
def reviews_course_read(request):
    if request.method == "GET":
        review_id = request.GET.get("id")
        if review_id is not None:
            try:
                review = ReviewsCourse.objects.get(id=review_id)
                serialized_review = {
                    "given_score": review.given_score,
                    "date": review.date,
                    "course": review.course.id,
                }
                return JsonResponse({"review": serialized_review})
            except ReviewsCourse.DoesNotExist:
                return JsonResponse({"error": "Review not found"}, status=404)
        else:
            return JsonResponse({"error": "Review ID parameter is missing"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['PUT'])
def reviews_course_update(request):
    if request.method == 'PUT':
        data = request.data
        review_id = data.get('id')
        try:
            review = ReviewsCourse.objects.get(id=review_id)
            review.given_score = data.get('given_score')
            review.date = data.get('date')
            review.course_id = data.get('course_id')
            review.save()
            return JsonResponse({'message': 'Review updated successfully'})
        except ReviewsCourse.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['DELETE'])
def reviews_course_delete(request):
    if request.method == 'DELETE':
        data = request.data
        review_id = data.get('id')
        try:
            review = ReviewsCourse.objects.get(id=review_id)
            review.delete()
            return JsonResponse({'message': 'Review deleted successfully'})
        except ReviewsCourse.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

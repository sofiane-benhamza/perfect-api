from django.http import JsonResponse
from .models import Quiz, Courses
from rest_framework.decorators import api_view # type: ignore

@api_view(["POST"])
def quiz_create(request):
    if request.method == "POST":
        data = request.data
        question = data.get("question")
        rep_A = data.get("rep_A")
        rep_B = data.get("rep_B")
        rep_C = data.get("rep_C")
        time_to_answer = data.get("time_to_answer")
        answer = data.get("answer")
        course_id = data.get("course_id")

        if not (question and rep_A and rep_B and rep_C and time_to_answer and answer and course_id):
            return JsonResponse({"error": "Missing required fields"}, status=400)

        try:
            course = Courses.objects.get(id=course_id)
            quiz = Quiz.objects.create(
                question=question,
                rep_A=rep_A,
                rep_B=rep_B,
                rep_C=rep_C,
                time_to_answer=time_to_answer,
                answer=answer,
                course=course
            )
            return JsonResponse(
                {"message": "Quiz created successfully"}, status=200
            )
        except Courses.DoesNotExist:
            return JsonResponse({"error": "Course not found"}, status=404)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['GET'])
def quiz_read(request):
    if request.method == "GET":
        quiz_id = request.GET.get("id")
        if quiz_id is not None:
            try:
                quiz = Quiz.objects.get(id=quiz_id)
                serialized_quiz = {
                    "question": quiz.question,
                    "rep_A": quiz.rep_A,
                    "rep_B": quiz.rep_B,
                    "rep_C": quiz.rep_C,
                    "time_to_answer": quiz.time_to_answer,
                    "answer": quiz.answer,
                    "course": quiz.course.id,
                }
                return JsonResponse({"quiz": serialized_quiz})
            except Quiz.DoesNotExist:
                return JsonResponse({"error": "Quiz not found"}, status=404)
        else:
            return JsonResponse({"error": "Quiz ID parameter is missing"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['PUT'])
def quiz_update(request):
    if request.method == 'PUT':
        data = request.data
        quiz_id = data.get('id')
        try:
            quiz = Quiz.objects.get(id=quiz_id)
            quiz.question = data.get('question')
            quiz.rep_A = data.get('rep_A')
            quiz.rep_B = data.get('rep_B')
            quiz.rep_C = data.get('rep_C')
            quiz.time_to_answer = data.get('time_to_answer')
            quiz.answer = data.get('answer')
            quiz.course_id = data.get('course_id')
            quiz.save()
            return JsonResponse({'message': 'Quiz updated successfully'})
        except Quiz.DoesNotExist:
            return JsonResponse({'error': 'Quiz not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['DELETE'])
def quiz_delete(request):
    if request.method == 'DELETE':
        data = request.data
        quiz_id = data.get('id')
        try:
            quiz = Quiz.objects.get(id=quiz_id)
            quiz.delete()
            return JsonResponse({'message': 'Quiz deleted successfully'})
        except Quiz.DoesNotExist:
            return JsonResponse({'error': 'Quiz not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

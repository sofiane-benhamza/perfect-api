from django.http import JsonResponse
from .models import Certificate
from rest_framework.decorators import api_view # type: ignore


@api_view(["POST"])
def certificate_create(request):
    if request.method == "POST":
        data = request.data
        completed_course_id = data.get("completed_course_id")
        user_student_id = data.get("user_student_id")

        if not (completed_course_id and user_student_id):
            return JsonResponse({"error": "Missing required fields"}, status=400)

        try:
            certificate = Certificate.objects.create(
                completed_course_id=completed_course_id,
                user_student_id=user_student_id
            )
            return JsonResponse(
                {"message": "Certificate created successfully"}, status=200
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['GET'])
def certificate_read(request):
    if request.method == "GET":
        certificate_id = request.GET.get("id")
        if certificate_id is not None:
            try:
                certificate = Certificate.objects.get(id=certificate_id)
                serialized_certificate = {
                    "completed_course_id": certificate.completed_course_id,
                    "user_student_id": certificate.user_student_id,
                }
                return JsonResponse({"certificate": serialized_certificate})
            except Certificate.DoesNotExist:
                return JsonResponse({"error": "Certificate not found"}, status=404)
        else:
            return JsonResponse({"error": "Certificate ID parameter is missing"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['PUT'])
def certificate_update(request):
    if request.method == 'PUT':
        data = request.data
        certificate_id = data.get('id')
        try:
            certificate = Certificate.objects.get(id=certificate_id)
            certificate.completed_course_id = data.get('completed_course_id')
            certificate.user_student_id = data.get('user_student_id')
            certificate.save()
            return JsonResponse({'message': 'Certificate updated successfully'})
        except Certificate.DoesNotExist:
            return JsonResponse({'error': 'Certificate not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['DELETE'])
def certificate_delete(request):
    if request.method == 'DELETE':
        data = request.data
        certificate_id = data.get('id')
        try:
            certificate = Certificate.objects.get(id=certificate_id)
            certificate.delete()
            return JsonResponse({'message': 'Certificate deleted successfully'})
        except Certificate.DoesNotExist:
            return JsonResponse({'error': 'Certificate not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

from django.http import JsonResponse

from authentication.models import UserStudent

def student_create(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        password = data.get('password')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        is_male = data.get('isMale')
        level = data.get('level')

        if name and password and email and phone and address and is_male and level:
            user_student = UserStudent.objects.create(
                name=name,
                password=password,
                email=email,
                phone=phone,
                address=address,
                is_male=is_male,
                level=level
            )
            return JsonResponse({'message': 'Student created successfully'})
        else:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def student_read(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        if email:
            try:
                student = UserStudent.objects.get(email=email)
                serialized_student = {
                    'name': student.name,
                    'email': student.email,
                    'phone': student.phone,
                    'address': student.address,
                    'is_male': student.is_male,
                    'level': student.level
                }
                return JsonResponse({'student': serialized_student})
            except UserStudent.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)
        else:
            return JsonResponse({'error': 'Email parameter is missing'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def student_update(request):
    if request.method == 'PUT':
        data = request.POST
        student_id = data.get('id')
        try:
            student = UserStudent.objects.get(pk=student_id)
            student.name = data.get('name')
            student.password = data.get('password')
            student.email = data.get('email')
            student.phone = data.get('phone')
            student.address = data.get('address')
            student.is_male = data.get('isMale')
            student.level = data.get('level')
            student.save()
            return JsonResponse({'message': 'Student updated successfully'})
        except UserStudent.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def student_delete(request):
    if request.method == 'DELETE':
        data = request.POST
        student_id = data.get('id')
        try:
            student = UserStudent.objects.get(pk=student_id)
            student.delete()
            return JsonResponse({'message': 'Student deleted successfully'})
        except UserStudent.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


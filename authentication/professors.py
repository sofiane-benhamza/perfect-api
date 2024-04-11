from django.http import JsonResponse
from authentication.models import UserProf

def professor_create(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        password = data.get('password')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        speciality = data.get('speciality')
        review_number = data.get('review_number')
        review_score = data.get('review_score')
        is_male = data.get('isMale')

        if name and password and email and phone and address and speciality and review_number and review_score and is_male:
            user_prof = UserProf.objects.create(
                name=name,
                password=password,
                email=email,
                phone=phone,
                address=address,
                speciality=speciality,
                review_number=review_number,
                review_score=review_score,
                isMale=is_male
            )
            return JsonResponse({'message': 'Professor created successfully'})
        else:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    
def professor_read(request):
     if request.method == 'GET':
        email = request.GET.get('email')
        if email:
            try:
                professor = UserProf.objects.get(email=email)
                serialized_professor = {
                    'name': professor.name,
                    'email': professor.email,
                    'phone': professor.phone,
                    'address': professor.address,
                    'speciality': professor.speciality,
                    'review_number': professor.review_number,
                    'review_score': professor.review_score,
                    'is_male': professor.isMale
                }
                return JsonResponse({'professor': serialized_professor})
            except UserProf.DoesNotExist:
                return JsonResponse({'error': 'Professor not found'}, status=404)
        else:
            return JsonResponse({'error': 'Email parameter is missing'}, status=400)
     else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    
def professor_update(request):
    
    if request.method == 'PUT':
        data = request.POST
        professor_id = data.get('id')
        try:
            professor = UserProf.objects.get(pk=professor_id)
            professor.name = data.get('name')
            professor.password = data.get('password')
            professor.email = data.get('email')
            professor.phone = data.get('phone')
            professor.address = data.get('address')
            professor.speciality = data.get('speciality')
            professor.review_number = data.get('review_number')
            professor.review_score = data.get('review_score')
            professor.isMale = data.get('isMale')
            professor.save()
            return JsonResponse({'message': 'Professor updated successfully'})
        except UserProf.DoesNotExist:
            return JsonResponse({'error': 'Professor not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405) 
      
    
def professor_delete(request):
    if request.method == 'DELETE':
        data = request.POST
        professor_id = data.get('id')
        try:
            professor = UserProf.objects.get(pk=professor_id)
            professor.delete()
            return JsonResponse({'message': 'Professor deleted successfully'})
        except UserProf.DoesNotExist:
            return JsonResponse({'error': 'Professor not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
from django.http import JsonResponse
from authentication.models import UserProf
import json

def professor_create(request):
      if request.method == 'POST':
        try:
            data = json.loads(request.body)  
            user_prof = UserProf.objects.create(
                name=data['name'],
                password=data['password'],
                etablissement=data.get('etablissement', ''),  
                email=data['email'],
                phone=data['phone'],
                address=data['address'],
                speciality=data['speciality'],
                review_number=data['review_number'],
                review_score=data['review_score'],
                isMale=data['isMale']
            )
            user_prof_json = {
                'id': user_prof.id,
                'name': user_prof.name,
                'etablissement': user_prof.etablissement,
                'email': user_prof.email,
                'phone': user_prof.phone,
                'address': user_prof.address,
                'speciality': user_prof.speciality,
                'review_number': user_prof.review_number,
                'review_score': user_prof.review_score,
                'isMale': user_prof.isMale
            }
            return JsonResponse({'message': 'Professor created successfully', 'user_prof': user_prof_json})
        except KeyError:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
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
                    'etablissement': professor.etablissement,
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
        try:
            data = json.loads(request.body)
            professor_id = data.get('id')
            if professor_id is not None:
                professor = UserProf.objects.get(pk=professor_id)
                
                professor.name = data.get('name')
                professor.password = data.get('password')
                professor.email = data.get('email')
                professor.etablissement = data.get('etablissement')
                professor.phone = data.get('phone')
                professor.address = data.get('address')
                professor.speciality = data.get('speciality')
                professor.review_number = data.get('review_number')
                professor.review_score = data.get('review_score')
                professor.isMale = data.get('isMale')

                
                professor.save()
                return JsonResponse({'message': 'Professor updated successfully'})
            else:
                return JsonResponse({'error': 'Professor ID is missing'}, status=400)
        except UserProf.DoesNotExist:
            return JsonResponse({'error': 'Professor not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

      
    
def professor_delete(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            professor_id = data.get('id')

            if professor_id is not None:
                professor = UserProf.objects.get(pk=professor_id)
                professor.delete()
                return JsonResponse({'message': 'Professor deleted successfully'})
            else:
                return JsonResponse({'error': 'Professor ID is missing'}, status=400)
        except UserProf.DoesNotExist:
            return JsonResponse({'error': 'Professor not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
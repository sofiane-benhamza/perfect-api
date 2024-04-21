from django.http import JsonResponse
import json
from authentication.models import Experience, UserProf
from rest_framework.decorators import api_view 

@api_view(['POST'])
def experience_create(request):
    if request.method == 'POST':
        try:
            data = request.data
            prof_email = data.get('prof_email')
            name = data.get('name')
            s_date = data.get('start_date')
            e_date = data.get('end_date')
            professor = UserProf.objects.get(email=prof_email)

            experience = Experience.objects.create(name=name, start_date=s_date, end_data=e_date, user_prof=professor)

            return JsonResponse({'message': 'Experience created successfully', 'id': experience.id})
        except KeyError:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['GET'])
def experience_read(request, experience_id):
    if request.method == 'GET':
        try:
            prof_email = request.GET.get("email")
            professor = UserProf.objects.get(email=prof_email)
            experiences = Experience.objects.get(user_prof=professor)

            return JsonResponse({experiences}, status=200)
        except Experience.DoesNotExist:
            return JsonResponse({'error': 'Experience not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['PUT'])
def experience_update(request, experience_id):
    if request.method in ['PUT', 'PATCH']:
        try:
            data = request.data
            prof_email = data.get('prof_email')
            old_exp_name = data.get('exp_name')
            new_exp_name = data.get('exp_name_new')
            s_date = data.get('start_date')
            e_date = data.get('end_date')
            professor = UserProf.objects.get(email=prof_email)
            experience = Experience.objects.get(user_prof=professor,name=old_exp_name) 
            experience.name=new_exp_name
            experience.start_date=s_date
            experience.end_date=e_date

            return JsonResponse({'message': 'Experience updated successfully'})
        except Experience.DoesNotExist:
            return JsonResponse({'error': 'Experience not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@api_view(['DELETE'])
def experience_delete(request, experience_id):
    if request.method == 'DELETE':
        data = request.GET
        try:
            prof_email = data.get("prof_email")
            exp_name = data.get("name")

            professor = UserProf.objects.get(email=prof_email)
            experience = Experience.objects.get(user_prof=professor, name=exp_name)
            experience.delete()
            return JsonResponse({'message': 'Experience deleted successfully'})
        except Experience.DoesNotExist:
            return JsonResponse({'error': 'Experience not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
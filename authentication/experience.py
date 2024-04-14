from django.http import JsonResponse
import json
from authentication.models import Experience

def experience_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            date = data.get('date')

            experience = Experience.objects.create(name=name, date=date)

            return JsonResponse({'message': 'Experience created successfully', 'id': experience.id})
        except KeyError:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def experience_read(request, experience_id):
    if request.method == 'GET':
        try:
            experience = Experience.objects.get(pk=experience_id)
            data = {
                'id': experience.id,
                'name': experience.name,
                'date': experience.date
            }
            return JsonResponse({'experience': data})
        except Experience.DoesNotExist:
            return JsonResponse({'error': 'Experience not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def experience_update(request, experience_id):
    if request.method in ['PUT', 'PATCH']:
        try:
            data = json.loads(request.body)
            name = data.get('name')
            date = data.get('date')

            experience = Experience.objects.get(pk=experience_id)
            experience.name = name
            experience.date = date
            experience.save()

            return JsonResponse({'message': 'Experience updated successfully'})
        except Experience.DoesNotExist:
            return JsonResponse({'error': 'Experience not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def experience_delete(request, experience_id):
    if request.method == 'DELETE':
        try:
            experience = Experience.objects.get(pk=experience_id)
            experience.delete()

            return JsonResponse({'message': 'Experience deleted successfully'})
        except Experience.DoesNotExist:
            return JsonResponse({'error': 'Experience not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
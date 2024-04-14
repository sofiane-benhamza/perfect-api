import json
from django.http import JsonResponse
from authentication.models import Diploma

def diploma_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            diploma = Diploma.objects.create(
                name=data['name'],
                date=data['date'],
            )
            diploma_json ={
                'id': diploma.id,
                'name':diploma.name,
                'date':diploma.date
            }
            return JsonResponse({'message':'diploma createg successfully','diploma': diploma_json})
        except KeyError:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
      

def diploma_read(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        if name:
            try:
                diploma = Diploma.objects.get(name=name)
                data = {
                    'id': diploma.id,
                    'name': diploma.name,
                    'date': diploma.date
                }
                return JsonResponse({'diploma': data})
            except Diploma.DoesNotExist:
                return JsonResponse({'error': 'Diploma not found'}, status=404)
        else:
            return JsonResponse({'error': 'Name parameter is missing'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    
def diploma_update(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            diploma_id = data.get('id')
            if diploma_id is not None:
                diploma =Diploma.objects.get(pk=diploma_id)
                
                diploma.name = data.get('name')
                diploma.date = data.get('date')
                
                diploma.save()
                return JsonResponse({'message': 'diploma updated successfully'})
            else:
                return JsonResponse({'error': 'diploma ID is missing'}, status=400)
        except Diploma.DoesNotExist:
            return JsonResponse({'error': 'diploma not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

            
            
           
            

def diploma_delete(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            diploma_id = data.get('id')
            
            if diploma_id is not  None:
                diploma = Diploma.objects.get(pk=diploma_id)
                diploma.delete()
            return JsonResponse({'message': 'Diploma deleted successfully'})
        except Diploma.DoesNotExist:
            return JsonResponse({'error': 'Diploma not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
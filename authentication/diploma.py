from django.http import JsonResponse
from authentication.models import Diploma

def diploma_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        diploma = Diploma.objects.create(name=name, date=date)
        return JsonResponse({'message': 'Diploma created successfully', 'id': diploma.id})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def diploma_read(request, diploma_id):
    if request.method == 'GET':
        try:
            diploma = Diploma.objects.get(pk=diploma_id)
            data = {
                'id': diploma.id,
                'name': diploma.name,
                'date': diploma.date
            }
            return JsonResponse({'diploma': data})
        except Diploma.DoesNotExist:
            return JsonResponse({'error': 'Diploma not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def diploma_update(request, diploma_id):
    if request.method in ['PUT', 'PATCH']:
        try:
            diploma = Diploma.objects.get(pk=diploma_id)
            name = request.POST.get('name')
            date = request.POST.get('date')
            diploma.name = name
            diploma.date = date
            diploma.save()
            return JsonResponse({'message': 'Diploma updated successfully'})
        except Diploma.DoesNotExist:
            return JsonResponse({'error': 'Diploma not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def diploma_delete(request, diploma_id):
    if request.method == 'DELETE':
        try:
            diploma = Diploma.objects.get(pk=diploma_id)
            diploma.delete()
            return JsonResponse({'message': 'Diploma deleted successfully'})
        except Diploma.DoesNotExist:
            return JsonResponse({'error': 'Diploma not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
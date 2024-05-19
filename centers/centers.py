from django.http import JsonResponse
from .models import Center
from rest_framework.decorators import api_view # type: ignore


@api_view(['POST'])
def center_create(request):
    if request.method == 'POST':
        data = request.data
        name = data.get('name')
        email = data.get('email')
        address = data.get('address')
        phone = data.get('phone')
        capacity_of_centers = data.get('capacity_of_centers')

        if name and address and email and phone and address and capacity_of_centers:
            
            user_center = Center.objects.create(
                name=name,
                address=address,
                email=email,
                phone=phone,
                capacity_of_centers=capacity_of_centers
            )
            return JsonResponse({'message': 'center created successfully'})
        else:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['GET'])
def center_read(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        if email:
            try:
                center = Center.objects.get(email=email)
                serialized_center = {
                    'name': center.name,
                    'email': center.email,
                    'address': center.address,
                    'phone': center.phone,
                    'capacity_of_centers': center.capacity_of_centers
                }
                return JsonResponse({'center': serialized_center})
            except Center.DoesNotExist:
                return JsonResponse({'error': 'center not found'}, status=404)
        else:
            return JsonResponse({'error': 'Email parameter is missing'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['PUT'])
def center_update(request):
    if request.method == 'PUT':
        data = request.POST
        center_id = data.get('email')
        try:
            center= Center.objects.get(id=center_id)
            center.name = data.get('name')
            center.email = data.get('email')
            center.address = data.get('address')
            center.phone = data.get('phone')
            center.capacity_of_centers = data.get('capacity_of_centers')
            center.save()
            return JsonResponse({'message': 'center updated successfully'})
        except Center.DoesNotExist:
            return JsonResponse({'error': 'center not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['DELETE'])
def center_delete(request):
    if request.method == 'DELETE':
        data = request.POST
        center_id = data.get('email')
        try:
            center = Center.objects.get(email=center_id)
            center.delete()
            return JsonResponse({'message': 'center deleted successfully'})
        except Center.DoesNotExist:
            return JsonResponse({'error': 'center not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


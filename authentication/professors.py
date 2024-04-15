from django.http import JsonResponse
from authentication.models import UserProf
from rest_framework.decorators import api_view


@api_view(["POST"])
def professor_create(request):
    if request.method == "POST":
        data = request.data
        name = data.get("name")
        password = data.get("password")
        email = data.get("email")
        etablissement = data.get("etablissement")
        phone = data.get("phone")
        address = data.get("address")
        is_male = data.get("isMale")
        speciality = data.get("speciality")

        if not (
            name
            and password
            and email
            and phone
            and address
            and is_male
            and speciality
            and etablissement
        ):
            return JsonResponse({"error": "Missing required fields"}, status=400)

        user_prof = UserProf.objects.create(
            name=name,
            password=password,
            email=email,
            etablissement=etablissement,
            phone=phone,
            address=address,
            is_male=is_male,
            speciality=speciality
        )
        if user_prof:
            return JsonResponse(
                {"message": "Professor created successfully"}, status=200
            )
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['GET'])
def professor_read(request):
    if request.method == "GET":
        email = request.GET.get("email")
        if email:
            try:
                professor = UserProf.objects.get(email=email)
                serialized_professor = {
                    "name": professor.name,
                    "email": professor.email,
                    "etablissement": professor.etablissement,
                    "phone": professor.phone,
                    "address": professor.address,
                    "speciality": professor.speciality,
                    "is_male": professor.is_male,
                }
                return JsonResponse({"professor": serialized_professor})
            except UserProf.DoesNotExist:
                return JsonResponse({"error": "Professor not found"}, status=404)
        else:
            return JsonResponse({"error": "Email parameter is missing"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)



@api_view(['PUT'])
def professor_update(request):
    if request.method == 'PUT':
        data = request.POST
        professor_id = data.get('email')
        try:
            professor= UserProf.objects.get(id=professor_id)
            professor.name = data.get('name')
            professor.phone = data.get('phone')
            professor.address = data.get('address')
            professor.is_male = data.get('isMale')
            professor.etablissement = data.get('etablissement')
            professor.speciality = data.get('speciality')
            professor.save()
            return JsonResponse({'message': 'Student updated successfully'})
        except UserProf.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@api_view(['DELETE'])
def professor_delete(request):
    if request.method == 'DELETE':
        data = request.POST
        professor_email = data.get('email')
        try:
            professor = UserProf.objects.get(email=professor_email)
            professor.delete()
            return JsonResponse({'message': 'Student deleted successfully'})
        except UserProf.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
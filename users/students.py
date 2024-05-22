from rest_framework.response import Response  # Use Response for consistency
from users.models import Student
from rest_framework.decorators import api_view
from tokenAuth.encryption import hash
from tokenAuth.views import create_token
from rest_framework.request import Request

@api_view(['POST'])
def create(request):
    data = request.data
    got_name = data.get('firstName') + "#" + data.get('lastName')
    got_password = data.get('password')
    got_email = data.get('email')
    got_phone = data.get('phone')
    got_address = data.get('address')
    got_is_male = data.get('isMale')
    got_level = data.get('level')

    if all([got_name, got_password, got_email, got_phone, got_address, got_is_male, got_level]):
        user_student = Student.objects.create(
            name=got_name,
            password=hash(got_password),
            email=got_email,
            phone=got_phone,
            address=got_address,
            is_male=got_is_male,
            level=got_level
        )
        return Response({'message': 'Student created successfully'}, status=200)
    else:
        return Response({'error': 'Missing required fields'}, status=400)

@api_view(['GET'])
def read(request):
    email = request.GET.get('email')
    if email:
        try:
            student = Student.objects.get(email=email)
            serialized_student = {
                'firstName': student.name.split("#")[0],
                'lastName': student.name.split("#")[1],
                'email': student.email,
                'phone': student.phone,
                'address': student.address,
                'level': student.level
            }
            return Response({'student': serialized_student})
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
    else:
        return Response({'error': 'Email parameter is missing'}, status=400)

@api_view(['PUT'])
def update(request):
    data = request.data
    email = data.get('email')
    if email:
        try:
            student = Student.objects.get(email=email)
            student.name = data.get('firstName') + "#" + data.get('lastName')
            student.phone = data.get('phone')
            student.address = data.get('address')
            student.level = data.get('level')
            student.save()
            return Response({'message': 'Student updated successfully'})
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
    else:
        return Response({'error': 'Email parameter is missing'}, status=400)

@api_view(['DELETE'])
def disconnect(request):
    email = request.GET.get('email')
    if email:
        try:
            student = Student.objects.get(email=email)
            student.delete()
            return Response({'message': 'Student deleted successfully'})
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
    else:
        return Response({'error': 'Email parameter is missing'}, status=400)

@api_view(['PATCH'])
def connect(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')

    if email and password:
        print(email, password)
        try:
            student = Student.objects.get(email=email)
            if student.password == hash(password):
                token = create_token(student, "student")
                return Response({"token": token}, status=200)
            else:
                return Response({'error': 'Invalid password'}, status=401)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=401)
    else:
        return Response({'error': 'Email and password are required'}, status=400)

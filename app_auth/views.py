from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout

# Signup
@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login
@api_view(["POST"])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        token = Token.objects.get_or_create(user=user)
        # role = determine_user_role(user) 
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)
    
# Role
# def determine_user_role(user):
#     if user.role == 'etudiant':
#         return 'Étudiant'
#     elif user.role == 'prof':
#         return 'Professeur'
#     elif user.role == 'admin':
#         return 'Administrateur'
#     else:
#         return 'Role inconnu'

# Logout
@api_view(["POST"])
def logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response({'message': 'Successfully logged out'})

@api_view(["GET"])
def TestView(request):
    return Response({"message": "TestView page"})
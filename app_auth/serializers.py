from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token, created = Token.objects.get_or_create(user=user)
        return user

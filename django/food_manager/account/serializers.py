from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=True, required=False, default='')
    first_name = serializers.CharField(allow_blank=True, required=False, default='')
    last_name = serializers.CharField(allow_blank=True, required=False, default='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user

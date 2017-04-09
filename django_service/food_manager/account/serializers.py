from django.contrib.auth.models import User
from rest_framework import serializers


def password_validator(password):
    if len(password) < 5:
        raise serializers.ValidationError('This password is too short. It must contain at least 5 characters.')


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=True, required=False, default='')
    first_name = serializers.CharField(allow_blank=True, required=False, default='')
    last_name = serializers.CharField(allow_blank=True, required=False, default='')
    password = serializers.CharField(
        allow_blank=True, required=False, write_only=True, default='',
        style={'input_type': 'password'},
        validators=(password_validator, )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        read_only_fields = ('username',)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance


class UserRegistrationSerializer(serializers.ModelSerializer):
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

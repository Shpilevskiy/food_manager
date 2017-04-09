from django.contrib.auth.models import User
from rest_framework import (
    generics,
    permissions,
    status
)
from rest_framework.response import Response

from account.serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    model = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'status': 'user {} successfully registered'.format(serializer.data['username'])
        },
            status=status.HTTP_201_CREATED, headers=headers
        )

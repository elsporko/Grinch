from rest_framework.generics import ListCreateAPIView
from .models import GrinchUser
from .serializers import GrinchUserSerializer
from rest_framework import status
from rest_framework.response import Response


class GrinchUserView(ListCreateAPIView):
    queryset = GrinchUser.objects.exclude(username='admin')
    serializer_class = GrinchUserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = GrinchUserSerializer(data=request.data)

        if serializer.is_valid():
            GrinchUser.objects.create_user(serializer.validated_data['username'],
                                           serializer.validated_data['password'],
                                           **kwargs)
            return Response({f'User {serializer.get_name()} has been created'},
                            status=status.HTTP_200_OK)
        else:
            return Response({f'Error: Could not create user ({serializer.get_name()}: {serializer.errors}'},
                            status=status.HTTP_400_BAD_REQUEST)

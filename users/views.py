from django.contrib.auth import login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, status, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import GrinchUserSerializer, GrinchLoginSerializer, GrinchUserRegisterSerializer
from .validations import custom_validation, validate_password, validate_username

from .models import GrinchUser

class GrinchUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GrinchUser.objects.exclude(is_staff=True, is_active=False)
    serializer_class = GrinchUserSerializer
    lookup_field = 'id'

class GrinchUserRegisterView(GenericAPIView):
    serializer_class =GrinchUserRegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = GrinchUserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GrinchUserLoginView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    serializer_class = GrinchLoginSerializer

    def post(self, request):
        data = request.data
        assert validate_username(data)
        assert validate_password(data)
        #serializer = GrinchLoginSerializer(data=data)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            #user = serializer.check_user(data)
            user = serializer.check_user(serializer.validated_data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class GrinchUserLogoutView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    serializer_class = GrinchUserSerializer

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

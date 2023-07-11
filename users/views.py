from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
#$from django.views.generic.list import ListView
from rest_framework.response import Response
from .models import GrinchUser
from .serializers import GrinchUserSerializer
from rest_framework import status
from django.contrib.auth.models import User

class GrinchUser(ListCreateAPIView):
    queryset = GrinchUser.objects.exclude(username='admin')
    serializer_class = GrinchUserSerializer
    
    def post(self, request):
        data = request.data.copy()
        user.objects.create_user(data.username, data,email, data.password)

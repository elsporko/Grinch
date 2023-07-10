from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
#$from django.views.generic.list import ListView
from rest_framework.response import Response
from .models import GrinchUser
from .serializers import GrinchUserSerializer
from rest_framework import status

class GrinchUser(ListAPIView):
    queryset = GrinchUser.objects.exclude(username='admin')
    serializer_class = GrinchUserSerializer


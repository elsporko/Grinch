from django.shortcuts import render
#from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from django.views.generic.list import ListView
from rest_framework.response import Response
from .models import GrinchUser
from .serializers import GrinchUserSerializer
from rest_framework import status

class GrinchUser(ListView):
    queryset = GrinchUser.objects.all()
    serializer_class = GrinchUserSerializer
    template_name = 'home.html'


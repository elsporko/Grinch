from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import PickList
from .serializers import PicklistSerializer
from rest_framework import status

class Picklists(ListCreateAPIView):
    queryset = PickList.objects.all()
    serializer_class = PicklistSerializer

class Picklist(RetrieveAPIView):
    queryset = PickList.objects.all()
    serializer_class = PicklistSerializer

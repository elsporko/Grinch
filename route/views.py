from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Route
#from rest_framework.decorators import action
from .serializers import RouteSerializer
from rest_framework import status

import logging
logger = logging.getLogger(__name__)

class RouteViewSet(RetrieveAPIView):
    queryset = Route.objects.filter(active=True)
    serializer_class = RouteSerializer

class RoutesViewSet(ListCreateAPIView):
    queryset = Route.objects.filter(active=True)
    serializer_class = RouteSerializer
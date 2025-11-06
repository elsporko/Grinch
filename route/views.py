from django.shortcuts import render

from .models import Route
from picklist.models import PickList
#from rest_framework.decorators import action
from .serializers import RouteSerializer
from rest_framework import viewsets,status

import logging
logger = logging.getLogger(__name__)

class RouteViewSet(viewsets.ModelViewSet):
    "Display a single route"
    queryset = Route.objects.filter(active=True)
    serializer_class = RouteSerializer


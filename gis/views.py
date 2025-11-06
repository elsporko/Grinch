from django.shortcuts import render
from .serializers import GISSerializer
from .models import GIS
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
import logging
logger = logging.getLogger(__name__)

class GISView(ListCreateAPIView):
    queryset = GIS.objects.all()
    serializer_class = GISSerializer

    def post (self, request):
        data = request.data.copy()

        serializer=self.get_serializer(data=data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
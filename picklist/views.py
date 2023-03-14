from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import PickList, Route
from .serializers import PicklistSerializer
from rest_framework import status

class Picklists(ListCreateAPIView):
    queryset = PickList.objects.all()
    serializer_class = PicklistSerializer

    def post(self, request):
        data = request.data.copy()
        data['route'] = Route.get_route_id_by_name(data['route'])

        serializer=self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class Picklist(RetrieveAPIView):
    queryset = PickList.objects.all()
    serializer_class = PicklistSerializer

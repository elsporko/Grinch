from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import PickList, Route
from .serializers import PicklistSerializer, RouteSerializer
from rest_framework import status

class PicklistsViewSet(ListCreateAPIView):
    queryset = PickList.objects.all()
    serializer_class = PicklistSerializer

    def post(self, request):
        data = request.data.copy()

        serializer=self.get_serializer(data=data)
        serializer.is_valid()
        # TODO - Gracefully handle serializer invalidation
        print(f'ERROR: {serializer.errors}')
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = request.data.copy()

        print(f'request: {request.__dict__}')
        serializer=self.get_serializer(data=data)
        serializer.is_valid()
        # TODO raise an error if there is a save error
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class PicklistViewSet(RetrieveAPIView):
    queryset = PickList.objects.all().order_by('route')
    serializer_class = PicklistSerializer

class Routes(ListCreateAPIView):
    queryset = Route.objects.filter(active=True)
    serializer_class = RouteSerializer

    def post (self, request):
        data = request.data.copy()

        serializer=self.get_serializer(data=data)
        serializer.is_valid()
        # TODO raise an error if there is a save error
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class Route(RetrieveAPIView):
    queryset = Route.objects.filter(active=True)
    serializer_class = RouteSerializer


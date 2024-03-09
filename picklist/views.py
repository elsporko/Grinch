#from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
#from rest_framework.decorators import action
from .models import PickList, Route
from .serializers import PicklistSerializer, RouteSerializer
from rest_framework import status

import logging
logger = logging.getLogger(__name__)

class PicklistsViewSet(ListCreateAPIView):
    queryset = PickList.objects.all()
    serializer_class = PicklistSerializer

    def post(self, request):
        data = request.data.copy()

        serializer=self.get_serializer(data=data)
        if not serializer.is_valid():
            # TODO - Gracefully handle serializer invalidation
            logger.error (f'ERROR: {serializer.errors}')
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = request.data.copy()

        logger.info(f'request: {request.__dict__}')
        serializer=self.get_serializer(data=data)
        serializer.is_valid()
        # TODO raise an error if there is a save error
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class PicklistViewSet(RetrieveAPIView):
    queryset = PickList.objects.all().order_by('route')
    serializer_class = PicklistSerializer

class RoutesViewSet(ListCreateAPIView):
    queryset = Route.objects.filter(active=True)
    serializer_class = RouteSerializer

#    @action(detail=True, methods=['put','post'])
#    def post (self, request):
#        data = request.data.copy()
#
#        serializer=self.get_serializer(data=data)
#        serializer.is_valid()
#        # TODO raise an error if there is a save error
#        serializer.save()
#        return Response(serializer.data, status=status.HTTP_200_OK)
#
#    def put (self, request):
#        data = request.data.copy()
#        record = Route.objects.get(abbrev=data['abbrev'])
#        record.active = data['active']
#        logger.info(f"put: {type(data)}")
#        logger.info(f"put(record): {record.__dict__}")
#        serializer=self.get_serializer(data=record.__dict__)
#        serializer.is_valid()
#        logger.info(f'serializer errors: {serializer.errors}')
#        serializer.update(Route, record.__dict__)
#        return Response(serializer.data, status=status.HTTP_200_OK)

        #return Response({"message": {'Could not save, Bad data.'}}, status=status.HTTP_400_BAD_REQUEST)

class RouteViewSet(RetrieveAPIView):
    queryset = Route.objects.filter(active=True)
    serializer_class = RouteSerializer


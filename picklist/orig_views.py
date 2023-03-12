from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PickList
from .serializers import PicklistSerializer

class PicklistAPIView (APIView):
    def get_object(self, id):
        try:
            return PickList.objects.get(id=id)
        except PickList.DoesNotExist:
            return None
        
    def get(self, request, id=None, *args, **kwargs):
        """
        List all picklist items
        """
        print(f'******* args: {args}')
        print(f'******* kwargs: {kwargs}')
        picklist = self.get_object(id=id)
        if not picklist:
            return Response(
                    {"res": f"Object with id {id} does not exists"},
                    status = status.HTTP_400_BAD_REQUEST
                   )

        print(f'***** picklist: {picklist}')
        serializer = PicklistSerializer(picklist)
        return (Response(serializer.data, status=status.HTTP_200_OK))

        #picklist = None
        #if id:
        #    print(f'***** id: {id}')
        #    picklist = self.get_object(id=id)
        #    if not picklist:
        #        return Response(
        #                {"res": f"Object with id {id} does not exists"},
        #                status = status.HTTP_400_BAD_REQUEST
        #               )

        #else:
        #    picklist = PickList.objects.all()
        #    print(f'***** picklist: 0 {picklist[0].__dict__}')

        #print(f'***** picklist: {picklist}')
        #serializer = PicklistSerializer(picklist)
        ##return (Response(serializer.data, status=status.HTTP_200_OK))

    def post(self, request, *args, **kwargs):
        """
        Create the Picklist with given picklist data
        """
        data = {
            'order_id' : request.data.get('order_id'),
            'pickup_date' : request.data.get('pickup_date'),
            'route' : request.data.get('route'),
            'first_name': request.data.get('first_name'),
            'last_name' : request.data.get('last_name'),
            'home_phone' : request.data.get('home_phone'),
            'email' : request.data.get('email'),
            'street_address' : request.data.get('street_address'),
            'where_is_it' : request.data.get('where_is_it'),
            'client_comment' : request.data.get('client_comment'),
            'admin_comment' : request.data.get('admin_comment'),
            'got_money' : request.data.get('got_money'),
            'got_tree' : request.data.get('got_tree'),
            }

        serializer = PicklistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def put(self, request, id, *args, **kwargs):
            picklist = self.get_object(id)

            if not picklist:
                return Response(
                        {"res": f'Picklist with id {id} does not exist'},
                        status = status.HTTP_400_BAD_REQUEST
                       )

                data = {
                    'order_id' : request.data.get('order_id'),
                    'pickup_date' : request.data.get('pickup_date'),
                    'route' : request.data.get('route'),
                    'first_name': request.data.get('first_name'),
                    'last_name' : request.data.get('last_name'),
                    'home_phone' : request.data.get('home_phone'),
                    'email' : request.data.get('email'),
                    'street_address' : request.data.get('street_address'),
                    'where_is_it' : request.data.get('where_is_it'),
                    'client_comment' : request.data.get('client_comment'),
                    'admin_comment' : request.data.get('admin_comment'),
                    'got_money' : request.data.get('got_money'),
                    'got_tree' : request.data.get('got_tree'),
                    }

                serializer = PicklistSerializer(instance=picklist, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_CREATED)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, id, *args, **kwargs):
            picklist = self.get_object(id)
            if not picklist:
                return Response({'res': f'Object with id {id} does not exist'})

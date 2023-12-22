from django.shortcuts import render
from .serializers import PicklistSerializer, RouteSerializer, GISSerializer

class GIS(ListCreateAPIView):
    queryset = GIS.objects.all()
    serializer_class = GISSerializer

    def post (self, request):
        data = request.data.copy()

        serializer=self.get_serializer(data=data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)



from rest_framework import serializers
from .models import GIS

class GISSerializer(serializers.ModelSerializer):

    class Meta:
        model = GIS
        fields = ['lat', 'lon', 'name']

from rest_framework import serializers

class GISSerializer(serializers.ModelSerializer):

    class Meta:
        model = GIS
        fields = ['lat', 'lon', 'name']

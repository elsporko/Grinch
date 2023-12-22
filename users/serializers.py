from rest_framework import serializers
from .models import GrinchUser

class GrinchUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    class Meta:
        model = GrinchUser
        fields = ['username', 'name', 'route', 'email', 'is_active']

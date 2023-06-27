from rest_framework import serializers
from .models import GrinchUser

class GrinchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrinchUser
        fields = ['username', 'first_name', 'last_name', 'route', 'email', 'active']

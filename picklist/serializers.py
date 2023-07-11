from rest_framework import serializers
from .models import PickList, Route

class PicklistSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'
    class Meta:
        model = PickList
        fields = ['order_id', 'pickup_date', 'route', 'name',
                  'home_phone', 'email', 'street_address',
                  'where_is_it', 'client_comment', 'admin_comment',
                  'got_money', 'got_tree',
                 ]

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['name', 'active']

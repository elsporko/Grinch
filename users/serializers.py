from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

GrinchUser = get_user_model()


class GrinchUserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = GrinchUser
        fields = '__all__'

    def create(self, clean_data):
        user_obj = GrinchUser.objects.create_user(username=clean_data['username'],
                                                  password=clean_data['password'])
        user_obj.save()
        return user_obj


class GrinchLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        user = authenticate(username=clean_data['username'], password=clean_data['password'])
        if not user:
            raise ValidationError('User not found')
        return user


class GrinchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrinchUser
        fields = '__all__'

    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

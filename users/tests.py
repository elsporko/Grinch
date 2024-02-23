import pytest
from django.contrib.auth import get_user_model, authenticate
import logging
logger = logging.getLogger(__name__)


class TestUsersManagers:
    @pytest.mark.django_db
    def test_create_user(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(username='testUser', password='1234')
        assert user.username == "testUser"
        assert user.is_active is True
        assert user.is_staff is False
        assert user.is_superuser is False
        authenticated_user = authenticate(username='testUser', password='1234')
        assert authenticated_user == user

    @pytest.mark.django_db
    def test_create_superuser(self):
        user_model = get_user_model()
        user = user_model.objects.create_superuser(username='testAdmin', password='admin')
        assert user.username == "testAdmin"
        assert user.is_active is True
        assert user.is_staff is True
        assert user.is_superuser is True
        authenticated_user = authenticate(username='testAdmin', password='admin')
        assert authenticated_user == user


class TestUsersLoginAPIs:

    def get_user_list(self, api_client, expected_return_code=200):
        url = '/api/users/'
        response = api_client.get(url, format='json')
        assert response.status_code == expected_return_code
        return response

    @pytest.mark.django_db
    def test_authentication(self, api_client):
        user_credentials = {
            'username': 'test',
            'password': 'test',
        }

        # Attempt to access users without credentials
        self.get_user_list(api_client, 403)

        # register a user
        url = '/register/'
        response = api_client.post(url, user_credentials)
        assert response.status_code == 201

        # login as user
        url = '/login/'
        response = api_client.post(url, user_credentials)
        assert response.status_code == 200

        response = self.get_user_list(api_client)
        assert len(response.data) == 4

        url = '/logout/'
        response = api_client.post(url, format='json')
        assert response.status_code == 200

        self.get_user_list(api_client, 403)

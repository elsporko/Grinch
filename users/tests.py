import pytest
from django.contrib.auth import get_user_model, authenticate


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
        print(f'new password: {user.password}')

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

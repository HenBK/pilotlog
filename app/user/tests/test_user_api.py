import pytest

from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


@pytest.mark.django_db
class TestPublicUserApi:
    """
    Test the public endpoint of the users API,
    public means unauthenticated users
    """

    def test_create_valid_user_success(self, client):
        """Test creating user with valid payload is successful"""

        payload = {
            'email': 'test@example.com',
            'password': 'testpass',
            'name': 'Test Name',
        }
        res = client.post(CREATE_USER_URL, payload)
        created_user = get_user_model().objects.get(email=payload['email'])

        # check response status code
        assert res.status_code == status.HTTP_201_CREATED

        # check the user is created in the database
        assert created_user.check_password(payload['password'])

        # check the password is not returned in the response
        assert 'password' not in res.data

    def test_user_with_email_already_exists(self, client):
        """Test creating a user that already exists fails"""

        payload = {
            'email': 'test@example.com',
            'password': 'testpass',
            'name': 'Test Name',
        }
        create_user(**payload)
        res = client.post(CREATE_USER_URL, payload)

        assert res.status_code == status.HTTP_400_BAD_REQUEST

    def test_password_too_short(self, client):
        """Test that the password must be more than 5 characters"""

        payload = {
            'email': 'test@example.com',
            'password': 'pw',
            'name': 'Test Name',
        }
        res = client.post(CREATE_USER_URL, payload)
        user_exists = get_user_model().objects.filter(
            email=payload['email'],
        ).exists()

        assert res.status_code == status.HTTP_400_BAD_REQUEST
        assert not user_exists

    def test_create_token_for_user(self, client):
        """Test that a token is created for the user"""

        user_details = {
            'email': 'test@example.com',
            'name': 'Test Name',
            'password': 'testpass',
        }

        create_user(**user_details)

        payload = {
            'email': user_details['email'],
            'password': user_details['password'],
        }

        res = client.post(TOKEN_URL, payload)

        assert res.status_code == status.HTTP_200_OK
        assert 'token' in res.data

    def test_create_token_invalid_credentials(self, client):
        """Test that token is not created if invalid credentials are given"""

        create_user(email='test@example.com', password='testpass')

        payload = {
            'email': 'wrong_email@example.com',
            'password': 'wrong_password',
        }

        res = client.post(TOKEN_URL, payload)

        assert res.status_code == status.HTTP_400_BAD_REQUEST
        assert 'token' not in res.data

    def test_create_token_with_blank_password(self, client):
        """Test that token is not created if user doesn't provide password"""

        payload = {
            'email': 'test@example.com',
            'password': '',
        }

        res = client.post(TOKEN_URL, payload)

        assert res.status_code == status.HTTP_400_BAD_REQUEST
        assert 'token' not in res.data

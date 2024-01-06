import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
class TestUserModel:

    def test_create_user_with_email(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        assert user.email == email
        assert user.check_password(password)

    def test_normalize_email(self):
        """Test the email for a new user is normalized"""

        sample_emails = [
            ('test1@EXAMPLE.com', 'test1@example.com'),
            ('TEST2@EXAMPLE.COM', 'TEST2@example.com'),
            ('test3@example.COM', 'test3@example.com'),
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'test123')

            assert user.email == expected

    def test_create_user_without_email_fails(self):
        """Test creating a new user without an email raises error"""

        with pytest.raises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        """Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        assert user.is_superuser
        assert user.is_staff

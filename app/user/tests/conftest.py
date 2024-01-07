import pytest

from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def normal_user():
    return mixer.blend(
        get_user_model(),
        is_superuser=False,
        is_staff=False,
        is_active=True,
    )


@pytest.fixture
def super_user():
    return mixer.blend(
        get_user_model(),
        is_superuser=True,
        is_staff=True,
        is_active=True,
    )

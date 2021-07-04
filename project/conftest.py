import pytest

from pytest_factoryboy import register
from tests.factories import PostFactory, UserFactory
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

register(PostFactory) 
register(UserFactory)
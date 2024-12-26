import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db  # This tells pytest to use the test database
def test_hello_world():
    client = Client()
    url = reverse('hello_world')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content.decode() == 'Hello, World!'


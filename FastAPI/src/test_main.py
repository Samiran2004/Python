import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_headers_with_all_headers():
    response = client.get(
        '/get_headers',
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'TestClient'
        }
    )
    assert response.status_code == 200
    assert response.json()['Accept'] == 'application/json'
    assert response.json()['Content-Type'] == 'application/json'

def test_get_headers_with_no_headers():
    response = client.get('/get_headers')
    assert response.status_code == 200
    assert response.json()['Accept'] is None
    assert response.json()['Content-Type'] is None

def test_get_headers_with_partial_headers():
    response = client.get(
        '/get_headers',
        headers={'Accept': 'text/html'}
    )
    assert response.status_code == 200
    assert response.json()['Accept'] == 'text/html'
    assert response.json()['Content-Type'] is None

def test_get_headers_response_structure():
    response = client.get('/get_headers')
    assert isinstance(response.json(), dict)
    assert 'Accept' in response.json()
    assert 'Content-Type' in response.json()
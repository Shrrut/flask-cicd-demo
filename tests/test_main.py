import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app.main import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello" in response.data

def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200

def test_add():
    client = app.test_client()
    response = client.get('/add/2/3')
    assert response.get_json()["result"] == 5
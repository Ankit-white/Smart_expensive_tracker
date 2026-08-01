from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_filter_expenses():
    response = client.get("/expenses?category=Food")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
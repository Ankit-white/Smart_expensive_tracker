from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_total_expenses():
    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert "total" in response.json()
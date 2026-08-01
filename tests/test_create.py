from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Dinner",
            "amount": 600,
            "category": "Food",
            "date": "2026-08-01"
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Dinner"
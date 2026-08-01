from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_delete_invalid_expense():
    response = client.delete("/expenses/invalid-id")

    assert response.status_code == 404
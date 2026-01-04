from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user_ok():
  response = client.post(
    "/users",
    json={
      "email": "test_for_test@example.com",
      "password": "123456"
    }
  )

  assert response.status_code == 200

  data = response.json()
  assert "id" in data
  assert data["email"] == "test_for_test@example.com"
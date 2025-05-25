from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/register", json={
        "name":"Diogo",
        "email":"Diogo1234@gmail.com",
        "login":"Apogavi",
        "password":"123456"
    })

    assert response.status_code == 200
    assert response.json()["email"] == "Diogo1234@gmail.com"

def test_login_user():
    response = client.post("/users/login", json={
        "identifier":"Apogavi",
        "password":"123456"
    })

    assert response.status_code == 200
    json_response = response.json()
    assert "access_token" in response.json()
    assert json_response["token_type"] == "bearer"
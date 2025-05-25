from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# USERS

# def test_create_user():
#     response = client.post("/users/register", json={
#         "email":"DioBrando@gmail.com",
#         "login":"DioBrando",
#         "password":"12345678"
#     })

#     assert response.status_code == 200
#     assert response.json()["email"] == "DioBrando@gmail.com"

# def test_login_user():
#     response = client.post("/users/login", json={
#         "identifier":"DioBrando@gmail.com",
#         "password":"12345678"
#     })

#     assert response.status_code == 200
#     json_response = response.json()
#     assert "access_token" in response.json()
#     assert json_response["token_type"] == "bearer"

# PRODUCTS

def test_create_product():
    response = client.post("/products/", json={
        "name":"Raquete Teste 2",
        "category":"Acessório",
        "price":12.00
    })

    print(response.json())
    assert response.status_code == 200

def test_list_product():
    response = client.get("/products/list")

    print(response.json())
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 1
    assert "id" in data[0]
    assert "name" in data[0]
    assert "category" in data[0]
    assert "price" in data[0]
    
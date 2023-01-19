import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate_addition():
    data = {"operator": "add", "num1": 5, "num2": 3}
    response = client.post("/calculate/", json=data)
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_calculate_subtraction():
    data = {"operator": "subtract", "num1": 5, "num2": 3}
    response = client.post("/calculate/", json=data)
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_calculate_multiplication():
    data = {"operator": "multiply", "num1": 5, "num2": 3}
    response = client.post("/calculate/", json=data)
    assert response.status_code == 200
    assert response.json() == {"result": 15}

def test_calculate_division():
    data = {"operator": "divide", "num1": 10, "num2": 2}
    response = client.post("/calculate/", json=data)
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_calculate_invalid_operator():
    data = {"operator": "foo", "num1": 5, "num2": 3}
    response = client.post("/calculate/", json=data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid operator"}

def test_calculate_invalid_input():
    data = {"operator": "add", "num1": "five", "num2": 3}
    response = client.post("/calculate/", json=data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid input"}

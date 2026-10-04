from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"E-Commerce API"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"OK"


def test_get_products():
    client = app.test_client()
    response = client.get("/products")

    assert response.status_code == 200

    data = response.get_json()
    assert len(data) == 3


def test_get_product():
    client = app.test_client()
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.get_json()["name"] == "Laptop"


def test_product_not_found():
    client = app.test_client()
    response = client.get("/products/99")

    assert response.status_code == 404
    assert response.get_json()["error"] == "Product not found"

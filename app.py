from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 75000},
    {"id": 2, "name": "Phone", "price": 45000},
    {"id": 3, "name": "Headphones", "price": 5000}
]


@app.route("/")
def home():
    return "E-Commerce API"


@app.route("/health")
def health():
    return "OK"


@app.route("/products")
def get_products():
    return jsonify(products)


@app.route("/products/<int:product_id>")
def get_product(product_id):
    product = next(
        (item for item in products if item["id"] == product_id),
        None
    )

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

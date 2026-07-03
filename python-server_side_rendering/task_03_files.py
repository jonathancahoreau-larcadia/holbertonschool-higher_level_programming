"""Flask application displaying products from JSON or CSV files."""

import csv
import json
from flask import Flask, render_template, request


app = Flask(__name__)


def read_json():
    """Read and return products from the JSON file."""
    with open("products.json", "r", encoding="utf-8") as file:
        return json.load(file)


def read_csv():
    """Read and return products from the CSV file."""
    with open("products.csv", "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


@app.route("/")
def home():
    """Display the home page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Display the about page."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Display the contact page."""
    return render_template("contact.html")


@app.route("/items")
def items():
    """Display the items page."""
    with open("items.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    items_list = data.get("items", [])

    return render_template("items.html", items=items_list)


@app.route("/products")
def products():
    """Display products from a JSON or CSV source."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    product_list = []
    error = None

    if source == "json":
        product_list = read_json()
    elif source == "csv":
        product_list = read_csv()
    else:
        error = "Wrong source"

    if product_id is not None and error is None:
        try:
            requested_id = int(product_id)
        except ValueError:
            product_list = []
            error = "Product not found"
        else:
            filtered_products = []

            for product in product_list:
                if int(product.get("id")) == requested_id:
                    filtered_products.append(product)

            product_list = filtered_products

            if not product_list:
                error = "Product not found"

    return render_template(
        "product_display.html",
        products=product_list,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

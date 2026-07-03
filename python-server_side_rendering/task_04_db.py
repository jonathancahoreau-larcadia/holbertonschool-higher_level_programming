#!/usr/bin/python3
"""Display product data from JSON, CSV, or SQLite using Flask."""

import csv
import json
import sqlite3

from flask import Flask, render_template, request


app = Flask(__name__)

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

def read_json():
    """Read products from the JSON file."""
    with open("products.json", "r", encoding="utf-8") as file:
        return json.load(file)


def read_csv():
    """Read products from the CSV file."""
    with open("products.csv", "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def read_sql():
    """Read products from the SQLite database."""
    connection = sqlite3.connect("products.db")

    try:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, name, category, price
            FROM Products
            """
        )

        rows = cursor.fetchall()

        return [dict(row) for row in rows]
    finally:
        connection.close()


@app.route("/products")
def products():
    """Display products using the selected data source."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    product_list = []
    error = None

    try:
        if source == "json":
            product_list = read_json()
        elif source == "csv":
            product_list = read_csv()
        elif source == "sql":
            product_list = read_sql()
        else:
            error = "Wrong source"

    except (OSError, json.JSONDecodeError, csv.Error):
        error = "Error reading data"

    except sqlite3.Error:
        error = "Database error"

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

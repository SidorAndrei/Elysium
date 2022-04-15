from flask import Flask, render_template, url_for
from dotenv import load_dotenv

import queries

load_dotenv()
app = Flask("Elysium")


@app.route("/")
def main_page():
    return render_template('base_template.html')


@app.route("/supermarkets")
def supermarkets_page():
    supermarkets = queries.get_all_supermarkets()
    return render_template("supermarkets_page.html", supermarkets=supermarkets)


@app.route("/supermarket/<supermarket_id>")
def supermarket_page(supermarket_id):
    products = queries.get_products_by_supermarket_id(supermarket_id)


def main():
    app.run(debug=False)


if __name__ == "__main__":
    main()

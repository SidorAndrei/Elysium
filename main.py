from flask import Flask, render_template, url_for, request, redirect, session
from dotenv import load_dotenv

import cryptography
import queries

import mailing
from json_response import json_response

load_dotenv()
app = Flask("Elysium")
app.secret_key = 'usef484ns94k/-2F2@indeed-L.A.S?'


@app.route("/")
def main_page():
    return render_template('main.html')


@app.route("/supermarkets")
def supermarkets_page():
    return render_template("supermarkets_page.html")


@app.route("/supermarket/<supermarket_id>")
def supermarket_page(supermarket_id):
    products = queries.get_products_by_supermarket_id(supermarket_id)
    return render_template("supermarkets_page.html", products=products)


@app.route("/categorii")
def categories_page():
    return render_template("search_page.html")


@app.route("/api/address")
def get_address():
    address = queries.get_address()
    return {"address": address}


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/test2")
def test2():
    return render_template("test2.html")


@app.route("/login")
def login_page():
    return render_template('login_page.html')


@app.route("/register")
def register_page():
    return render_template('register_page.html')


@app.route("/login-request", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    user = queries.get_user(username)[0]
    print(user)
    if cryptography.verify_password(password, user["password"]):
        session.update({
            "name": user["name"]
        })
        return redirect(url_for('main_page'))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('main_page'))


@app.route("/register-request", methods=["GET", "POST"])
def register_request():
    reg_request = {
        'name': request.form['full_name'],
        'username': request.form['username'],
        'password': request.form['password'],
        'email': request.form['email'],
        'phone_number': request.form['phone'],
        'address': request.form['street'] + ' ' + request.form['street_number'] + ', ' +
                   request.form['city'] + ' ' + request.form['postal_code'],
        'status': request.form['status']
    }
    print(reg_request)
    reg_request.update({
        'password': cryptography.hash_password(reg_request['password'])
    })
    queries.insert_register_request(reg_request)
    mailing.send_request_mail(reg_request['email'], reg_request['name'])
    return redirect(url_for('main_page'))


@app.route('/confirm-request/<request_id>')
def confirm_request(request_id):
    user = queries.confirm_register_request(request_id)[0]
    print(user)
    mailing.send_confirmation_mail(user["email"], user["name"], session["name"])
    return redirect(url_for('review_register_requests'))


@app.route('/reject-request/<request_id>')
def reject_request(request_id):
    user = queries.reject_register_request(request_id)[0]
    print(user)
    mailing.send_rejected_mail(user["email"], user["name"], session["name"], "No accurate details")
    return redirect(url_for('review_register_requests'))


@app.route('/api/check_user/<username>/<password>')
def api_check_user(username, password):
    print(username, password)
    try:
        user = queries.get_user(username)[0]
        user.update({
            "password_match": cryptography.verify_password(password, user["password"])
        })
        return {"user": user}
    except IndexError:
        return {"user": {"username": None}}


@app.route('/review-register-requests')
def review_register_requests():
    requests = queries.get_register_requests()
    return render_template('register_requests.html', requests=requests)


def main():
    app.run(debug=False)


if __name__ == "__main__":
    main()

    # mailing.send_rejected_mail('sidor.marian.andrei3001@gmail.com', "Loredana", "Sidor Andrei", "Noisy")
    # mailing.send_confirmation_mail('sidor.marian.andrei3001@gmail.com', "Sidor Andrei", "Loredana Stefania")
    # mailing.send_request_mail("sidor.marian.andrei3001@gmail.com", "Sidor Andrei")

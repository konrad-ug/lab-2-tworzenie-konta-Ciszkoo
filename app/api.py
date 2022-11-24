from flask import Flask, request, jsonify
from app.AccountsRegister import AccountsRegister
from app.Account import Account

app = Flask(__name__)


@app.route("/account/create_account", methods=["POST"])
def create_account():
    data = request.get_json()
    print(f"Received data - creating account: {data}")
    account = Account(data["name"], data["surname"], data["pesel"])
    AccountsRegister.add_account(account)
    return jsonify("Account created!"), 201


@app.route("/account/number_of_accounts", methods=["GET"])
def number_of_accounts():
    return jsonify(AccountsRegister.number_of_accounts()), 200


@app.route("/account/find_account/<pesel>", methods=["GET"])
def find_account(pesel):
    account = AccountsRegister.find_account(pesel)
    if account:
        return jsonify(account.__dict__), 200
    return jsonify("Account not found!"), 404

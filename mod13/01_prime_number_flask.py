from math import isqrt
from flask import Flask, jsonify


def is_prime_number(number) -> bool:
    if number <= 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(2, isqrt(number) + 1):
        if number % i == 0:
            return False

    return True


app = Flask(__name__)


@app.route("/alkuluku/<int:number>", methods=["GET"])
def prime_route(number):
    result = {"number": number, "isPrime": is_prime_number(number)}
    return jsonify(result), 200


app.run(host="127.0.0.1", port=5000, debug=True)

from math import isqrt
from flask import Flask


def is_prime_number(number) -> bool:
    if number <= 1:
        return False
    elif number % 2 == 0:
        return True
    else:
        for i in range(2, isqrt(number) + 1):
            if number % i == 0:
                return False
    return True


app = Flask(__name__)


@app.route("/alkuluku/<int:number>", methods=["GET"])
def prime_route(number):
    json = {"Number": number, "isPrime": is_prime_number(number)}
    return json

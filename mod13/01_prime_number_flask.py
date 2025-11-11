from math import isqrt
from flask import Flask, json, Response
from functools import wraps


class ApiResponse(Response):
    default_mimetype = "application/json"

    def __init__(
        self,
        data=None,
        message=None,
        status=200,
        success=True,
        error_detail=None,
        **kwargs,
    ):
        if success:
            body = {"ok": True, "message": message or "Success", "data": data}
        else:
            body = {"ok": False, "message": message or "Unkown error"}
            if error_detail:
                body["error"] = str(error_detail)

        super().__init__(
            response=json.dumps(body),
            status=status,
            mimetype=self.default_mimetype,
            **kwargs,
        )

    @classmethod
    def ok(cls, data=None, message="OK", status=200):
        return cls(success=True, data=data, message=message, status=status)

    @classmethod
    def error(cls, message="Internal server error", status=500, error_detail=None):
        return cls(
            success=False, message=message, status=status, error_detail=error_detail
        )


def safe_route(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, Response):
                return result
            return ApiResponse.ok(result)
        except ValueError as e:
            return ApiResponse.error(
                message="Invalid input", error_detail=e, status=400
            )
        except Exception as e:
            return ApiResponse.error(error_detail=e)

    return wrapper


def is_prime_number(number) -> bool:
    if number < 2:
        return False

    if number % 2 == 0:
        return False

    for i in range(2, isqrt(number) + 1):
        if number % i == 0:
            return False

    return True


class ApiConfig:
    SECRET_KEY = "temp_secret_key"
    DEBUG = True
    TESTING = False
    PORT = 5001
    HOST = "127.0.0.1"


app = Flask(__name__)
app.config.from_object(ApiConfig)


@app.route("/alkuluku/<number>", methods=["GET"])
@safe_route
def prime_route(number):
    integer = int(number)
    return {"number": number, "isPrime": is_prime_number(integer)}


@app.route("/favicon.ico", methods=["GET"])
def favicon():
    return "", 204


@app.errorhandler(404)
def handle_not_found(e):
    return ApiResponse.error(message="Endpoint not found", error_detail=e, status=404)


if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])

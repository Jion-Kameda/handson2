import logging
from decimal import Decimal, InvalidOperation

import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

ERR_REQUIRED = "A and B are required."
ERR_NUMERIC = "A and B must be numeric values."
ERR_DIV_ZERO = "B must not be zero."


def _to_plain_text_number(value: Decimal) -> str:
    text = format(value.normalize(), "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    if text == "-0":
        return "0"
    return text


def _parse_query_params(req: func.HttpRequest) -> tuple[Decimal | None, Decimal | None, func.HttpResponse | None]:
    a_raw = req.params.get("A")
    b_raw = req.params.get("B")

    if a_raw is None or b_raw is None:
        return None, None, func.HttpResponse(ERR_REQUIRED, status_code=400, mimetype="text/plain")

    try:
        a = Decimal(a_raw)
        b = Decimal(b_raw)
    except InvalidOperation:
        return None, None, func.HttpResponse(ERR_NUMERIC, status_code=400, mimetype="text/plain")

    return a, b, None


@app.route(route="multiply", methods=["GET"])
def multiply(req: func.HttpRequest) -> func.HttpResponse:
    a, b, error = _parse_query_params(req)
    if error is not None:
        logging.warning("multiply validation error")
        return error

    result = a * b
    logging.info("multiply succeeded")
    return func.HttpResponse(_to_plain_text_number(result), status_code=200, mimetype="text/plain")


@app.route(route="divide", methods=["GET"])
def divide(req: func.HttpRequest) -> func.HttpResponse:
    a, b, error = _parse_query_params(req)
    if error is not None:
        logging.warning("divide validation error")
        return error

    if b == Decimal("0"):
        logging.warning("divide validation error: division by zero")
        return func.HttpResponse(ERR_DIV_ZERO, status_code=400, mimetype="text/plain")

    result = a / b
    logging.info("divide succeeded")
    return func.HttpResponse(_to_plain_text_number(result), status_code=200, mimetype="text/plain")

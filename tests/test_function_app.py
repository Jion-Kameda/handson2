import azure.functions as func

from function_app import divide, multiply


def _make_request(params: dict[str, str]) -> func.HttpRequest:
    return func.HttpRequest(method="GET", url="http://localhost/api/test", params=params, body=b"")


def _body_text(response: func.HttpResponse) -> str:
    return response.get_body().decode("utf-8")


def test_multiply_success() -> None:
    response = multiply(_make_request({"A": "3", "B": "4"}))
    assert response.status_code == 200
    assert _body_text(response) == "12"


def test_divide_success() -> None:
    response = divide(_make_request({"A": "5", "B": "2"}))
    assert response.status_code == 200
    assert _body_text(response) == "2.5"


def test_missing_query_params() -> None:
    response = multiply(_make_request({"A": "3"}))
    assert response.status_code == 400
    assert _body_text(response) == "A and B are required."


def test_non_numeric_params() -> None:
    response = multiply(_make_request({"A": "x", "B": "2"}))
    assert response.status_code == 400
    assert _body_text(response) == "A and B must be numeric values."


def test_divide_by_zero() -> None:
    response = divide(_make_request({"A": "10", "B": "0"}))
    assert response.status_code == 400
    assert _body_text(response) == "B must not be zero."

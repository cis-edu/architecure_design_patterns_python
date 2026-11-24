from datetime import datetime
from functools import wraps
from typing import Any, Callable

from flask import request

from singleton.request import Requests


def request_log(view: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(view)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        started = datetime.now()
        requests = Requests.get_instance()
        requests.count += 1
        requests.last_path = request.path
        try:
            return view(*args, **kwargs)
        finally:
            requests.last_seconds = (datetime.now() - started).total_seconds()
            print("request", requests.count, request.path, requests.last_seconds)

    return wrapper


__all__ = ["request_log"]

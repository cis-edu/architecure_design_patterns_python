from functools import wraps
from datetime import datetime

from flask import request
from singleton.requests import Requests

REQUESTS = Requests.get_instance()


def request_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        started = datetime.now()
        REQUESTS.count += 1
        REQUESTS.last_path = request.path

        try:
            return func(*args, **kwargs)
        finally:
            REQUESTS.last_seconds = (
                datetime.now() - started
            ).total_seconds()

            print(
                "request",
                REQUESTS.count,
                request.path,
                REQUESTS.last_seconds,
            )

    return wrapper

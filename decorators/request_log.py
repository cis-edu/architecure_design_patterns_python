from flask import request
from datetime import datetime
from functools import wraps
from singleton.requests import Requests


def request_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        requests = Requests.get_instance()

        started = datetime.now()
        requests.count += 1
        requests.last_path = request.path

        try:
            return func(*args, **kwargs)
        finally:
            requests.last_seconds = (datetime.now() - started).total_seconds()
            print("request", requests.count, request.path, requests.last_seconds)

    return wrapper

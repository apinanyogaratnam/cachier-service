import json

from datetime import datetime, timedelta

from flask import request
from flask_restful import Resource

from sqlite_driver import SqliteDriver


class Root(Resource):
    def __init__(self: 'Root') -> None:
        self.sqlite_driver = SqliteDriver('cache.db')

    def get(self: 'Root') -> dict:
        cache_key: str = request.args.get('cache_key', type=str, default=None)

        if not cache_key: return None

        data = self.read_data(cache_key)

        return {'value': data}

    def post(self: 'Root') -> dict:
        body: dict = request.get_json()

        if not body:
            print('no body received')
            return False

        print('received body', body)

        cache_key: str | None = body.get('cache_key', None)
        cache_value: object | None = body.get('cache_value', None)
        cache_expiry: int | None = body.get('cache_expiry', None)

        if not cache_key or not cache_value:
            print('no cache key or value received')
            return False

        is_saved_successfully: bool = self.write_data(cache_key, cache_value, cache_expiry)

        return {'is_saved_successfully': is_saved_successfully}

    def read_data(self: 'Root', key: str) -> object | None:
        if not key: return None

        return self.sqlite_driver.read_data(key)

    def write_data(self: 'Root', key: str, value: object, cache_expiry: int | None = None) -> bool:
        if not key: return False

        return self.sqlite_driver.write_data(key, value, cache_expiry)

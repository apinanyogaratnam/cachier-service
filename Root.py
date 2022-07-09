import json

from datetime import datetime, timedelta

from flask import request
from flask_restful import Resource


class Root(Resource):
    def __init__(self: 'Root') -> None:
        pass

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

    def read_data(self: 'Root', key: str) -> object:
        if not key:
            print('no key to read')
            return None

        with open('data.json', 'r') as f:
            data: dict = json.load(f)

        cache_metadata = data.get(key, None)

        if not cache_metadata: return None

        cache_value = cache_metadata.get('value', None)
        cache_expiry = cache_metadata.get('expiry', None)

        if not cache_value: return None
        if not cache_expiry: return cache_value

        expiry_date: datetime = datetime.fromisoformat(cache_expiry)
        current_date: datetime = datetime.now()

        cache_expired: bool = current_date > expiry_date
        if cache_expired: return None

        return cache_value

    def write_data(self: 'Root', key: str, value: object, cache_expiry: int | None) -> bool:
        data: dict = request.get_json()

        if not data:
            print('no data to write')
            return False

        try:
            with open('data.json', 'r') as f:
                data: dict = json.load(f)

            if not cache_expiry:
                encoded_expiry = ''
            else:
                expiry_date: datetime = datetime.now() + timedelta(seconds=cache_expiry)
                encoded_expiry: str = expiry_date.isoformat()

            # update the data
            data[key] = {
                'value': value,
                'expiry': encoded_expiry,
            }

            with open('data.json', 'w') as f:
                json.dump(data, f)
        except Exception as error:
            print(error)
            return False

        return True

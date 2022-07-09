import json

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

        cache_key: str = body.get('cache_key', None)
        cache_value: object = body.get('cache_value', None)

        if not cache_key or not cache_value:
            print('no cache key or value received')
            return False

        is_saved_successfully: bool = self.write_data(cache_key, cache_value)

        return {'is_saved_successfully': is_saved_successfully}

    def read_data(self: 'Root', key: str) -> object:
        if not key:
            print('no key to read')
            return None

        with open('data.json', 'r') as f:
            data: dict = json.load(f)

        return data.get(key, None)

    def write_data(self: 'Root', key: str, value: object) -> bool:
        data: dict = request.get_json()

        if not data:
            print('no data to write')
            return False

        try:
            with open('data.json', 'w') as f:
                # read the existing data
                data: dict = json.load(f)

                # update the data
                data[key] = value

                # write the new data
                json.dump(data, f)
        except Exception as error:
            print(error)
            return False

        return True

import json

from flask import request
from flask_restful import Resource


class Root(Resource):
    def __init__(self: 'Root') -> None:
        pass

    def get(self: 'Root') -> object:
        cache_key: str = request.args.get('cache_key', type=str, default=None)

        if not cache_key: return None

        # TODO: get data from a file
        data = None

        return data

    def post(self: 'Root') -> bool:
        body: object = request.get_json()

        if not body: return False

        cache_key: str = body.get('cache_key', type=str, default=None)
        cache_value: object = body.get('cache_value', type=object, default=None)

        if not cache_key or cache_value: return False

        is_saved_successfully: bool = self.write_data(cache_key, cache_value)

        return is_saved_successfully

    def read_data(self: 'Root', key: str) -> object:
        if not key: return None

        with open('data.json', 'r') as f:
            data: dict = json.load(f)

        return data.get(key, None)

    def write_data(self: 'Root', key: str, value: object) -> bool:
        data: dict = request.get_json()

        if not data: return False

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

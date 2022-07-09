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
        cached_data: object = body.get('cached_data', type=object, default=None)

        if not cache_key or cached_data: return False

        # TODO: save body to a file
        saved_successfully: bool = True

        return saved_successfully

    def read_data(self: 'Root') -> object:
        pass

    def write_data(self: 'Root') -> bool:
        pass

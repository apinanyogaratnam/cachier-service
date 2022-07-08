from flask import request
from flask_restful import Resource


class Root(Resource):
    def __init__(self: 'Root') -> None:
        pass

    def get(self: 'Root') -> object:
        return 'Hello World!'

    def post(self: 'Root') -> bool:
        body: object = request.get_data()

        # TODO: save body to a file

        saved_successfully: bool = True

        return saved_successfully

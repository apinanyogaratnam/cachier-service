from flask_restful import Resource


class Root(Resource):
    def __init__(self: 'Root') -> None:
        pass

    def get(self: 'Root') -> str:
        return 'Hello World!'

    def post(self: 'Root') -> str:
        return 'Hello World!'

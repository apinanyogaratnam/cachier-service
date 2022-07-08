from flask_restful import Resource


class Root(Resource):
    def __init__(self: 'Root') -> None:
        pass

    def get(self: 'Root') -> object:
        return 'Hello World!'

    def post(self: 'Root') -> bool:
        return True

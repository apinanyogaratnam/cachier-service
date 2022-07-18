from flask import request
from flask_restful import Resource

from json_driver import JsonDriver
from pickle_driver import PickleDriver
from sqlite_driver import SqliteDriver
from ram_driver import RamDriver
from module_types import Driver


class Root(Resource):
    def __init__(self: 'Root') -> None:
        self.sqlite_driver = SqliteDriver('cache.db')
        self.json_driver = JsonDriver('data.json')
        self.pickle_driver = PickleDriver('cache.pickle')
        self.ram_driver = RamDriver()

    def get(self: 'Root') -> dict:
        cache_key: str = request.args.get('cache_key', type=str, default=None)
        driver: str = request.args.get('driver', type=str, default=None)

        if not cache_key: return None

        driver: Driver = self.get_driver(driver)
        data = self.read_data(cache_key, driver)

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
        driver: str | None = body.get('driver', None)

        if not cache_key or not cache_value:
            print('no cache key or value received')
            return False

        driver: Driver = self.get_driver(driver)
        is_saved_successfully: bool = self.write_data(cache_key, cache_value, cache_expiry, driver)

        return {'is_saved_successfully': is_saved_successfully}

    def read_data(self: 'Root', key: str, driver: Driver = None) -> object | None:
        if not key: return None

        if not driver:
            return self.ram_driver.read_data(key)

        return driver.read_data(key)

    def write_data(
        self: 'Root', key: str, value: object, cache_expiry: int | None = None, driver: Driver = None
    ) -> bool:
        if not key: return False

        if not driver:
            return self.ram_driver.write_data(key, value, cache_expiry)

        return driver.write_data(key, value, cache_expiry)

    def get_driver(self: 'Root', driver: str) -> Driver:
        # TODO: convert to enum
        driver_map = {
            'sqlite': self.sqlite_driver,
            'json': self.json_driver,
            'pickle': self.pickle_driver,
            'ram': self.ram_driver,
        }

        return driver_map.get(driver, None)

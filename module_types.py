from sqlite_driver import SqliteDriver
from json_driver import JsonDriver
from pickle_driver import PickleDriver


class Driver(SqliteDriver, JsonDriver, PickleDriver):
    pass

from enum import Enum

from sqlite_driver import SqliteDriver
from json_driver import JsonDriver
from pickle_driver import PickleDriver
from ram_driver import RamDriver


class Driver(SqliteDriver, JsonDriver, PickleDriver, RamDriver):
    pass


class DriverType(Enum):
    SQLITE = 'sqlite'
    JSON = 'json'
    PICKLE = 'pickle'
    RAM = 'ram'

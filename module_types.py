from enum import Enum

from sqlite_driver import SqliteDriver
from json_driver import JsonDriver
from pickle_driver import PickleDriver
from ram_driver import RamDriver


class Driver(SqliteDriver, JsonDriver, PickleDriver, RamDriver):
    pass


class DriverType(Enum):
    SQLITE = 1
    JSON = 2
    PICKLE = 3
    RAM = 4

    def __eq__(self, other):
        return self.value == other.value

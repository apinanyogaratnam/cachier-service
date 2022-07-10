class SqliteDriver:
    def __init__(self: 'SqliteDriver', filename: str) -> None:
        self.filename = filename

    def read_data(self: 'SqliteDriver', key: str) -> object | None:
        pass

    def write_data(self: 'SqliteDriver', key: str, value: str, expiry: int | None = None) -> bool:
        pass

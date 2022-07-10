from utility import get_sqlite_connection, query_sqlite_database


class SqliteDriver:
    def __init__(self: 'SqliteDriver', filename: str) -> None:
        self.filename = filename

    def read_data(self: 'SqliteDriver', key: str) -> object | None:
        if not key: return None

        with get_sqlite_connection(self.filename) as connection:
            query = f'''
                SELECT cache_value, NOW() > cache_expiry AS is_cache_expired
                FROM cache
                WHERE cache_key = '{key}';
            '''

            result = query_sqlite_database(connection, query)

            if not result: return None

        is_cache_expired = result[0]['is_cache_expired']

        if is_cache_expired: return None

        return result[0]['cache_value']

    def write_data(self: 'SqliteDriver', key: str, value: str, expiry: int | None = None) -> bool:
        pass

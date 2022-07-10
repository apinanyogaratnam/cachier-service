import json
import sqlite3

from datetime import datetime, timedelta

from utility import get_sqlite_connection, query_sqlite_database, write_sqlite_database


class SqliteDriver:
    def __init__(self: 'SqliteDriver', filename: str) -> None:
        self.filename = filename

    def read_data(self: 'SqliteDriver', key: str) -> object | None:
        if not key: return None

        with get_sqlite_connection(self.filename) as connection:
            query = f'''
                SELECT cache_value, DATETIME(cache_expiry) AS cache_expiry
                FROM cache
                WHERE cache_key = '{key}';
            '''

            result = query_sqlite_database(connection, query).to_dict('records')

            if not result: return None

            print('result', result)

            is_cache_expired = datetime.utcnow() > datetime.strptime(result[0]['cache_expiry'], '%Y-%m-%d %H:%M:%S')

            print('is_cache_expired', is_cache_expired)

            if is_cache_expired:
                self.delete_data(key, connection)
                return None

        return json.loads(result[0]['cache_value'])

    def write_data(self: 'SqliteDriver', key: str, value: str, expiry: int | None = None) -> bool:
        if not key: return False

        with get_sqlite_connection(self.filename) as connection:
            if not expiry:
                encoded_expiry = 'NULL'
            else:
                expiry_date: datetime = datetime.utcnow() + timedelta(seconds=expiry)
                encoded_expiry: str = expiry_date.isoformat()

            value = json.dumps(value)
            # update the data
            insert_data_query = f'''
                INSERT INTO cache (cache_key, cache_value, cache_expiry)
                VALUES ('{key}', '{value}', '{encoded_expiry}');
            '''

            return write_sqlite_database(connection, insert_data_query)

    def delete_data(self: 'SqliteDriver', key: str, connection: sqlite3.Connection) -> bool:
        delete_data_query = f'''
            DELETE FROM cache
            WHERE cache_key = '{key}';
        '''

        return write_sqlite_database(connection, delete_data_query)

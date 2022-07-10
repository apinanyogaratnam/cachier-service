import sqlite3

import pandas as pd


def get_sqlite_connection(filename: str) -> sqlite3.Connection:
    connection: sqlite3.Connection = sqlite3.connect(filename)
    return connection


def query_sqlite_database(connection: sqlite3.Connection, query: str) -> object:
    table: pd.DataFrame = pd.read_sql_query(query, connection)
    return table


def write_sqlite_database(connection: sqlite3.Connection, query: str) -> bool:
    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            connection.commit()
            return True
        except Exception as error:
            print(error)
            connection.rollback()
            return False

# TODO: create write_sqlite_database_with_parameters() function

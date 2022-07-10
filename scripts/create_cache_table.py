import sqlite3


def main():
    connection = sqlite3.connect('cache.db')

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS cache (
            cache_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            created TIMESTAMP NOT NULL,
            cache_key TEXT NOT NULL,
            cache_value TEXT,
            cache_expiry TIMESTAMP
        );
    '''

    try:
        print('Creating table...')
        connection.execute(create_table_query)
        connection.commit()
        print('Table created successfully')
    except Exception as error:
        print(error)
        connection.rollback()
    finally:
        connection.close()
        print('Connection closed')


if __name__ == '__main__':
    main()

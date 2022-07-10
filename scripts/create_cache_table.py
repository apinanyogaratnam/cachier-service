import sqlite3


def main():
    connection = sqlite3.connect('cache.db')

    drop_table_query = 'DROP TABLE IF EXISTS cache;'

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS cache (
            cache_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP_UTC NOT NULL,
            cache_key TEXT NOT NULL,
            cache_value TEXT,
            cache_expiry TIMESTAMP
        );
    '''

    try:
        print('dropping table...')
        connection.execute(drop_table_query)
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

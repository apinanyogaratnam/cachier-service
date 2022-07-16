from datetime import datetime, timedelta

ram_storage = {}


class RamDriver:
    def __init__(self: 'RamDriver') -> None:
        pass

    def read_data(self: 'RamDriver', key: str) -> object | None:
        if not key:
            print('no key to read')
            return None

        cache_metadata = ram_storage.get(key, None)

        if not cache_metadata: return None

        cache_value = cache_metadata.get('value', None)
        cache_expiry = cache_metadata.get('expiry', None)

        if not cache_value: return None
        if not cache_expiry: return cache_value

        expiry_date: datetime = datetime.fromisoformat(cache_expiry)
        current_date: datetime = datetime.utcnow()

        cache_expired: bool = current_date > expiry_date
        if cache_expired: return None

        return cache_value

    def write_data(self: 'RamDriver', key: str, value: object, cache_expiry: int | None = None) -> bool:
        try:
            expiry_date = None
            if cache_expiry:
                expiry_date: datetime = datetime.now() + timedelta(seconds=cache_expiry)

                # update the data
                ram_storage[key] = {
                    'value': value,
                    'expiry': expiry_date,
                }
        except Exception as error:
            print(error)
            return False

        return True

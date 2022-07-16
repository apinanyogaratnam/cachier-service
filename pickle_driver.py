import pickle

from datetime import datetime, timedelta


class PickleDriver:
    def __init__(self: 'PickleDriver', filename: str) -> None:
        self.filename = filename

    def read_data(self: 'PickleDriver', key: str) -> object | None:
        if not key:
            print('no key to read')
            return None

        with open(self.filename, 'r') as f:
            data: dict = pickle.load(f)

        cache_metadata = data.get(key, None)

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

    def write_data(self: 'PickleDriver', key: str, value: object, cache_expiry: int | None = None) -> bool:
        try:
            with open(self.filename, 'r') as f:
                data: dict = pickle.load(f)

            expiry_date = None
            if cache_expiry:
                expiry_date: datetime = datetime.now() + timedelta(seconds=cache_expiry)

            # update the data
            data[key] = {
                'value': value,
                'expiry': expiry_date,
            }

            with open(self.filename, 'w') as f:
                pickle.dump(data, f)
        except Exception as error:
            print(error)
            return False

        return True

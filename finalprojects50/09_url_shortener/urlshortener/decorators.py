import functools

def cache(func):
    _cache = {}

    @functools.wraps(func)
    def wrapper(self, short_code, *args, **kwargs):
        if short_code in _cache:
            print(f"⚡ Cache hit for '{short_code}'")
            return _cache[short_code]
        result = func(self, short_code, *args, **kwargs)
        if result is not None:
            _cache[short_code] = result
        return result

    return wrapper

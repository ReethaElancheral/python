# gradecalc/utils.py

def memoize(func):
    cache = {}

    def wrapper(self, *args):
        if self.student_id in cache:
            return cache[self.student_id]
        result = func(self, *args)
        cache[self.student_id] = result
        return result

    return wrapper

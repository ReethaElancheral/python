import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ Time Taken: {round(end - start, 2)} seconds")
        return result
    return wrapper

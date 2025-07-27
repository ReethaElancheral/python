_memory = None

def store(value):
    global _memory
    _memory = value

def recall():
    return _memory

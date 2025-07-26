
# 8. Multi-Step Data Cleaner (Chained Decorators) 
# Objective: Clean raw data using multiple decorators. 
# Requirements: 
#  One decorator removes nulls 
#  Another strips whitespace 
#  Another converts all strings to lowercase 
#  Chain all decorators for preprocessing 


from functools import wraps
def remove_nulls(func):
    @wraps(func)
    def wrapper(data):
        return func([x for x in data if x is not None])
    return wrapper

def strip_whitespace(func):
    @wraps(func)
    def wrapper(data):
        return func([x.strip() for x in data])
    return wrapper

def to_lowercase(func):
    @wraps(func)
    def wrapper(data):
        return func([x.lower() for x in data])
    return wrapper

@remove_nulls
@strip_whitespace
@to_lowercase
def clean_data(data):
    return data

raw = ["  Hello  ", None, " WoRLD ", "  PYTHON "]
print(clean_data(raw))

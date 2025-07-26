# 18. HTML Formatter for Web Output 
# Objective: Wrap function output in HTML tags. 
# Requirements: 
#  Use decorators to add <div>, <p>, <h1>, etc. 
#  Chain decorators to simulate templates 
#  Support @html_wrapper("h2") 

from functools import wraps

def html_wrapper(tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator

@html_wrapper("div")
@html_wrapper("p")
@html_wrapper("h2")
def get_web_content():
    return "Welcome to our wedding invitation website!"

# Example usage:
print(get_web_content())

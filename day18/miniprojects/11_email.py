# 11. Email Sending Simulator with Logging and Retry 
# Objective: Decorate email sending functions to handle retries and logging. 
# Requirements: 
#  Chain @retry and @log 
#  Retry 2 times if email fails 
#  Log status on each attempt



from functools import wraps
def log_email(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(f"Email Status: Success")
            return result
        except Exception as e:
            print(f"Email Status: Fail - {e}")
            raise
    return wrapper

def retry_email(max_retries=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 2):
                try:
                    print(f"Attempt {attempt}")
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_retries + 1:
                        print("Email failed permanently.")
        return wrapper
    return decorator

@retry_email(2)
@log_email
def send_email(to):
    if to != "valid@example.com":
        raise ValueError("Invalid recipient")
    print(f"Email sent to {to}")

send_email("valid@example.com")
send_email("fail@example.com")

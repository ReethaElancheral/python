# 17. API Call Simulator

# Use Case: Simulate calling external APIs. 
# Exception Handling Goals:
# Simulate TimeoutError or ConnectionError
# Use custom InvalidResponseError
# Retry logic inside try-except loop
# Use finally to log attempts

import random
import logging
import time

# Setup logging
logging.basicConfig(filename="api_calls.log", level=logging.INFO, format='%(asctime)s - %(message)s')

# Custom Exception
class InvalidResponseError(Exception):
    pass

def simulate_api_call():
    """Simulate different outcomes of an API call."""
    outcomes = ['success', 'timeout', 'connection_error', 'invalid_response']
    result = random.choice(outcomes)
    time.sleep(1)  # Simulate network delay
    if result == 'timeout':
        raise TimeoutError("API call timed out.")
    elif result == 'connection_error':
        raise ConnectionError("Failed to connect to the API.")
    elif result == 'invalid_response':
        raise InvalidResponseError("Received invalid response from API.")
    else:
        return {"status": "success", "data": "Sample API data"}

def api_call_with_retries(max_retries=3):
    attempts = 0
    while attempts < max_retries:
        try:
            attempts += 1
            print(f"Attempt {attempts} to call API...")
            response = simulate_api_call()
        except (TimeoutError, ConnectionError, InvalidResponseError) as e:
            logging.error(f"Attempt {attempts} failed: {e}")
            print(f"❌ Attempt {attempts} failed: {e}")
            time.sleep(1)  # wait before retry
        else:
            print("✅ API call successful!")
            print(f"Response: {response}")
            break
        finally:
            logging.info(f"Attempt {attempts} completed.")
    else:
        print("🚫 All attempts failed. Please try again later.")

if __name__ == "__main__":
    api_call_with_retries()

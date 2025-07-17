from logger import get_logger
logger = get_logger(__name__)
logger.info("Started")


# 45. Simulate a module reload using `importlib.reload()` after dynamically updating a function.

import mymod
import importlib
importlib.reload(mymod)




# 47. module.py
print(__name__)
if __name__ == "__main__":
    print("Running as script")

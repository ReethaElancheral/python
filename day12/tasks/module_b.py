# 10. Create two separate modules and call functions from one module inside the other.

from module_a import foo

def bar():
    print("bar from module_b")
    foo()

if __name__ == "__main__":
    bar()

from functools import wraps

def decorator_function(func):
    @wraps(func)
    def wrapper():
        return func()
    return wrapper


class decorator_class:
    def __init__(self, func):
        self.func = func
    def __call__(self):
        print("Hello world")
        return self.func()

@decorator_class
@decorator_function
def print_name():
    return ("Hello")

print(print_name())

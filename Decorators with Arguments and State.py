#Decorators with Arguments and State
from functools import wraps

def counter_decorator(max_count):
    def decorator(func):
        count = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal count
            if count >= max_count:
                print("Function call limit reached.")
                return None
            count += 1
            return func(*args, **kwargs)

        return wrapper
    return decorator

@counter_decorator(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")
greet("Dave")

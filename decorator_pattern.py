# decorator_pattern.py

# Base function
def greet(name):
    return f"Hello, {name}!"

# Decorator function
def excited_decorator(func):
    def wrapper(name):
        result = func(name)
        return result + " 😃🎉"
    return wrapper

# Decorator function 2
def uppercase_decorator(func):
    def wrapper(name):
        result = func(name)
        return result.upper()
    return wrapper

# Applying decorators
greet = excited_decorator(greet)
greet = uppercase_decorator(greet)

# Client code
if __name__ == "__main__":
    print(greet("Anil"))
def before_after(func):
    def wrapper(name):
        print("Before")
        func(name)
        print("After")
    return wrapper

def greet(name):
    print(f"Hello {name}")

greet("Shekhar")

print(greet.__name__)

@before_after
def greet(name):
    print(f"Hello {name}")

greet("Shekhar")

print(greet.__name__)
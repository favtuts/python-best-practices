def before_after(func):
    def wrapper(name):
        print("Before")
        func(name)
        print("After")
    return wrapper

@before_after
def greet(name):
    print(f"Hello {name}")


greet("shekhar")
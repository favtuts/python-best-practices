def before_after(func):
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")

    return wrapper


@before_after
def greet(name="Shekhar"):
    print(f"Hello {name}")


greet()
greet("joey")
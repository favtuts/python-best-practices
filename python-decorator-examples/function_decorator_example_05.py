import random

def do_thrice(func):
    print(f"Adding decorator to {func.__name__}")

    def wrapper():
        return (func(), func(), func())

    return wrapper


@do_thrice
def roll_dice():
    return random.randint(1, 6)

print(roll_dice())
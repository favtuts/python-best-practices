def prefix(prefix):
    def hello(name):
        print(f"{prefix} Hello, {name}!")
    return hello

print_warning = prefix("Warning :")

def reverse(func):
    def reverse_caller(text):
        func(text[::-1])

    return reverse_caller

rev_print = reverse(print)
rev_print("Hello Shekhar!")

rev_print = reverse(print_warning)
rev_print("Shekhar!")
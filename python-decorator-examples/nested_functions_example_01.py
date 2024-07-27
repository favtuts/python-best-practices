def prefix(prefix):
    def hello(name):
        print(f"{prefix} Hello, {name}!")
    return hello

print_debug = prefix("DEBUG :")
print_debug("shekhar")

print_warning = prefix("Warning :")
print_warning("Opps!")
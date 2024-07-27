def add_one(number):
    return number + 1

def multiply_10(number):
    return number * 10

function_list = [add_one, multiply_10]

print(add_one(10))
print(multiply_10(10))

print(function_list[0](10))
print(function_list[1](10))
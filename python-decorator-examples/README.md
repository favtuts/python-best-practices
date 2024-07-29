# Mastering Function Decorators in Python
* https://tuts.heomi.net/mastering-function-decorators-in-python/

# Nested function example

```python
def prefix(prefix):
    def hello(name):
        print(f"{prefix} Hello, {name}!")
    return hello

print_debug = prefix("DEBUG :")
print_debug("shekhar")

print_warning = prefix("Warning :")
print_warning("Opps!")
```

Output
```sh
$ python nested_functions_example_01.py 
DEBUG : Hello, shekhar!
Warning : Hello, Opps!!
```

# Creating Function Decorators

```python
def reverse(func):
    def reverse_caller(text):
        func(text[::-1])

    return reverse_caller

rev_print = reverse(print)
rev_print("Hello Shekhar!")

rev_print = reverse(print_warning)
rev_print("Shekhar!")
```

Output
```sh
$ python function_decorator_example_01.py 
!rahkehS olleH
Warning : Hello, !rahkehS!
```

Now this function `reverse()` is taking a function reference as a parameter and returning a function.
This is what we call a Decorator, it’s a function that takes a function as parameter, modifies it and returns the function.

Another way to do that is as following
```python
@reverse
def greet(name):
    print(f"Hello {name}")

greet("Shekhar")
```

This is exactly the same as `greet=reverse(greet)`. The `@reverse` is just a syntax to make things tidy and easier to read

The general template to make a decorator is as follows
```python
def decorator_name(func):
    def wrapper(func):
        #DO SOMETHING
    return wrapper
```

# Decorator Excercise

Let’s write a decorator that will Print “BEFORE” runs the function and print “AFTER”.
```python
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
```

Output
```sh
$ python function_decorator_example_02.py 
Before
Hello shekhar
After
```

# Handling arguments in Decorators

One interesting thing to notice here is that when we add our decorator to the function, the name of the function changes to the wrapper. This shows that when we use the decorated function, we are actually using the wrapper function from the decorator.

We will face a error if we try to make default argument or try to pass more than one argument to our decorated function. To solve these kinds of issues we use `*args` and `**kwargs`, they translate to argument and keyword arguments respectively.

Unpacking operators:
- `*` Expands any variable as List
- `**` Expands any variable as Dictionary

The `*args` enables us to send any number of arguments to the function and `**kwargs` enables us to pass in any number of keyworded arguments when calling the function.

`"args"` and `"kwargs"` is the general naming convention, You can use any other name following the same `*` and `**` pattern and it will work the same way.

# Using Args and Kwargs in Decorators


```python
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
```

Output:
```sh
$ python function_decorator_example_04.py 
Before
Hello Shekhar
After
Before
Hello joey
After
```


# Measuring Performance of other functions

Let's see what are some real use cases in which decorators are extremely useful.

Suppose you have many functions in your code and you want to optimise your code. Now instead of writing the code for getting the runtime and memory usage for each function, we can simply write a decorator and apply it to all the functions we want to test.

we are calculating function runtime using `perf_counter` (It's just like a `stopwatch`) and calculating memory usage using `tracemalloc` function


```python
from functools import wraps
import tracemalloc
from time import perf_counter 

def measure_performance(func):
    @wraps(func)  # It is a inbuilt decorator in python
    # When used, the decorated function name remains the same

    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f"Function: {func.__name__}")
        print(
            f"Memory usage:\t\t {current / 10**6:.6f} MB \n"
            f"Peak memory usage:\t {peak / 10**6:.6f} MB "
        )
        print(f"Time elapsed is seconds: {finish_time - start_time:.6f}")
        print(f'{"-"*40}')
        tracemalloc.stop()

    return wrapper


@measure_performance
def function1():
    lis = []
    for a in range(1000000):
        if a % 2 == 0:
            lis.append(1)
        else:
            lis.append(0)


@measure_performance
def function2():
    lis = [1 if a % 2 == 0 else 0 for a in range(1000000)]


function1()
function2()
```
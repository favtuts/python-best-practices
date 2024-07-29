from functools import wraps
import tracemalloc
from time import perf_counter

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



"""
$ python measure_performance_decorator.py
Function: function1
Memory usage:            0.000000 MB
Peak memory usage:       8.448768 MB
Time elapsed is seconds: 0.329556
----------------------------------------
Function: function2
Memory usage:            0.000000 MB
Peak memory usage:       8.448920 MB
Time elapsed is seconds: 0.294334
----------------------------------------
"""
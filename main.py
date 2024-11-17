#!/usr/bin/python
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Function {func.__name__!r} took: {end_time - start_time:.4f} sec')
        return result
    return wrapper
@timer
def example_function(n):
    return f"The sum is {sum(range(n))}"
print(example_function(100000), '\n')

def some_decorator(func):
    def wrapper():
        print(f'Running "{func.__name__}" function')
        func()
    return wrapper
@some_decorator
def do_this():
    print('Doing this.')

@some_decorator
def do_that():
    print('Doing that.')

do_this()                   ## parsed to @
do_that()                   ## parsed to @

# A decorator is a function that gets called before another function

import functools

def my_decorators(func):
    @functools.wraps(func)
    def function_that_runs_fun():
        print("Im the decorator")
        func()
        print("After the decorator")
    return function_that_runs_fun

@my_decorators
def my_function():
    print("I'm the function!")

my_function()
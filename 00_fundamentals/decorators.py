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

##

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            if number == 55:
                print("In the decorator ======")
            else:
                func(*args, *kwargs)
            print("=======After the decorator!")
        return function_that_runs_func
    return my_decorator

# Decorators can accept arguments, many arguments, so always pass in *arg and *kwargs
@decorator_with_arguments(55)
def my_function_too(x, y):
    print("hello from function_too")
    print(x + y)

my_function_too(77, 89)
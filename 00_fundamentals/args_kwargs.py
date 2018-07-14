
# function accepts two arguments
def my_method(arg1, arg2):
    return arg1 + arg2

# pass in two arguments to function
my_method(5, 6)

# function accepts 5 arguments, this is poopy
def my_long_method(arg1,arg2,arg3,arg4,arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5

# pass in 5 arguments to function
my_long_method(3, 5, 67, 8, 9)

def my_list_additions(list_arg):
    return sum(list_arg)

# better way use *args
def addition_simplified(*args):
    return sum(args)

addition_simplified(1, 2, 3, 4, 5, 6, 7, 8)


def what_are_args(*args):
    print(args)

# kwargs returns a set
def what_are_kwargs(**kwargs):
    print(kwargs)

what_are_args(12, 34, 454)
what_are_kwargs(name="Manny", location="Johannesburg")
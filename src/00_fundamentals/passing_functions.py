def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 55

# print(methodception(add_two_numbers))

# Lambda function, anonymous function
# print(methodception(lambda: 44 + 99))

my_list = [22, 33, 44, 667, 9]
print(list(filter(lambda x: x != 33, my_list)))


# these two function are identical
(lambda x: x * 3)(5)

def f(x):
    return x * 3

f(5)
# these two function are identical


# list comprehension
print(x for x in my_list if x != 33)
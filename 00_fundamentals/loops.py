my_string = "hello"

# bad ->
# print(my_variable[0])
# print(my_variable[1])
# print(my_variable[2])
# print(my_variable[3])
# print(my_variable[4])

# my_string is an iterable, stings/list/sets/tuples
for character in my_string:
    print(character)

my_list = [1, 2, 3, 4, 5]

for number in my_list:
    print(number ** 2)
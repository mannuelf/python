should_continue = True
if should_continue:
    print("Continue...")


people_you_know = ["John", "Max", "Mary"]
person = input("Enter the persoon you know: ")

if person in people_you_know:
    print("You know {}!".format(person))
else:
    print("You don't {}!".format(person))


# Exercise
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
def even_numbers(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return print(evens)

even_numbers(numbers)

# Modify the below method so that "Quit" is returned if the choice parameter is "q".
# Don't remove the existing code
def user_menu(choice):
    if choice == "a":
        return "Add"
    if choice == "q":
        return "Quit"

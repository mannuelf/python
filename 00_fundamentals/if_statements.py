should_continue = True
if should_continue:
    print("Continue...")


# people_you_know = ["John", "Max", "Mary"]
# person = input("Enter the persoon you know: ")

# if person in people_you_know:
#     print("You know {}!".format(person))
# else:
#     print("You don't {}!".format(person))


def who_do_you_know():
    people = input("What people do you know, comma seperated: ")
    people_list = people.split(",")
    people_without_spaces = [person.strip() for person in people.split(",")]
    return people_list

def ask_user():
    person = input("Enter a name of someone you know: ")
    if person in who_do_you_know():
        print("You know this person {} !".format(person))

ask_user()

# Exercise 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
def even_numbers(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return print(evens)

# even_numbers(numbers)

# Modify the below method so that "Quit" is returned if the choice parameter is "q".
# Don't remove the existing code
def user_menu(choice):
    if choice == "a":
        return "Add"
    if choice == "q":
        return "Quit"

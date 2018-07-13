# should_continue = True
# if should_continue:
#     print("Continue...")


people_you_know = ["John", "Max", "Mary"]
person = input("Enter the persoon you know: ")

if person in people_you_know:
    print("You know {}!".format(person))
else:
    print("You don't {}!".format(person))
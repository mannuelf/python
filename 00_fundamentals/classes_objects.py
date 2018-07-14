lottery_player_dict = {
    'name': 'Manny',
    'numbers': (5 ,9, 12, 3, 1, 21)
}

# a class is a blueprint, what data every lottery player has
class LotteryPlayer:
    def __init__(self, name):
        self.name = "Manny",
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)


# new up a lottery player, 
# creates an object from that class
player_one = LotteryPlayer("John")
player_one.numbers = (9, 10, 11)
player_two = LotteryPlayer("Jack")

# print(player_one.name == player_two.name)
# print(player_one.name)
# print(player_two.name)
# print(player_one.numbers)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks) 

anna = Student("Jose", "Unisa")
anna.marks.append(56)
anna.marks.append(36)
anna.marks.append(7)
print(anna.average())
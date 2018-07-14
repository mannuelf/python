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
# print(anna.average())


class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        items = {
            'name': name,
            'price': price
        }
        self.items.append(items)
        
    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        # total = 0
        # for items in self.items:
        #     total += items['price']
        # return total
        return sum([item['price'] for item in self.items])

shop = Store()
print(shop)
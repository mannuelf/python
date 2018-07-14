my_set = {1, 3, 5}
my_dict = { 'name': 'Manny', 'age': 36, 'grades': [13, 45, 66, 90] }
another_dict = {1: 15, 2: 75, 3: 150 }

lottery_player = {
    'name': 'Manny',
    'numbers': {13, 45, 66, 23, 22}
}

universities = {
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'USA'
    },
}

aSum = sum(lottery_player['numbers'])

print(aSum)

lottery_player['name'] = 'JoJo'
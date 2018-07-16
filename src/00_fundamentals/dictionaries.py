my_set = {1, 3, 5}
my_dict = {'name': 'Manny', 'age': 36, 'grades': [13, 45, 66, 90]}
another_dict = {1: 15, 2: 75, 3: 150}

lottery_player = [
    {
        'name': 'Manny',
        'numbers': (13, 45, 66, 23, 22)
    },
    {
        'name': 'Johnny',
        'numbers': (13, 45, 66, 23, 22)
    }
]

universities = {
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'USA'
    }
}

aSum = sum(lottery_player['numbers'])
print(aSum)

lottery_player['name'] = 'JoJo'

lottery_player[0].total()
lottery_player.total()

# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = [
    {
        'name': 'Jose',
        'school': 'Computing',
        'grades': (66, 77, 88)
    },
    {
        'name': 'Jack',
        'school': 'Mathematics',
        'grades': (88, 97, 68)
    }
]

print(student[0]['grades'])

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = data[0]['grades'] #always use data argument otherwise you will end using the global variable which is wrong    
    return print(sum(grades) / len(grades))

average_grade(student)

# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total = total + sum(student[0]['grades'])
        count = count + len(student[0]['grades'])
    return total / count

average_grade_all_students(student)
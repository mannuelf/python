
grade_one = 77
grade_two = 80
grade_three = 90
# print((grade_one + grade_two + grade_three) / 3)

# List
gradesA = [99, 88, 78, 55, 22, 10]
# print(sum(gradesA) / len(gradesA))

# Tuple
# Tuple are immutable, cannot increase its size
gradesB = (99, 88, 78, 55, 22, 10)
# print(gradesB)

# Sets
# unique and unordered
gradesC = {99, 12, 54, 52, 52}
# print(gradesC)

gradesA.append([00,90])
print(gradesA)

gradesB = gradesB + (102,) #eval right side first, leave comma in if only one element
print(gradesB)

print(gradesA[2])

gradesA[0] = 999

print(gradesB)

gradesC.add(888)
gradesC.add(999)

## Set operations

your_lottery_numbers = {1, 2, 3, 4, 5, 6}
winning_numbers = {1, 3, 5, 7, 9, 11}

# print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
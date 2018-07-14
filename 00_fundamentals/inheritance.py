class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return print(sum(self.marks) / len(self.marks))
    
    @classmethod
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school, salary)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school) # call super class, which will set properties from the parent class aka inheritance
        self.salary = salary

anna = WorkingStudent("Anna", "Oxford", 100)
print(anna.salary)

friend = WorkingStudent.friend(anna, "Greg", 99)
print(friend.name)
print(friend.school)
print(friend.salary)
# print(friend.salary) # AttributeError: 'Student' object has no attribute 'salary'

## 


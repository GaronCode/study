class Student:
    def __init__(self,num, grade):
        self.number = num
        self.grade = grade
        
class Group:
    def __init__(self, quantity, stud_constructor, name = 1):
        self.students = [stud_constructor(x) for x in range(1, quantity if quantity>=1 else 1)]
        self.name = name
    
    def average_score(self):
        return sum([x.grade for x in self.students]) / len(self.students)
    
    def full_name(self):
        return 'Группа №{}'.format(self.name)

    def print(self):
        print(self.full_name)
        print('Колличество студентов: ', len(self.students))
        print('Средний балл: ', self.average_score())
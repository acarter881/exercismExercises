class School:
    def __init__(self):
        self.d = {}

    def add_student(self, name, grade):
        self.studentName = name
        self.studentGrade = grade

        self.d.setdefault(name, grade)

    def roster(self):
        return list(dict(sorted(self.d.items(), key=lambda x: (x[1], x[0]))).keys())

    def grade(self, grade_number):
        return sorted([name for name, grade in self.d.items() if grade == grade_number])

school = School()
school.add_student(name="Peter", grade=2)
school.add_student(name="Anna", grade=1)
school.add_student(name="Barb", grade=1)
school.add_student(name="Zoe", grade=2)
school.add_student(name="Alex", grade=2)
school.add_student(name="Jim", grade=3)
school.add_student(name="Charlie", grade=1)

#print(school.roster())
#print(school.grade(2))
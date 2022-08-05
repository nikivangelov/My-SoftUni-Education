class Class:

    def __init__(self, name, students_count=22):
        self.class_name = name
        self.students_count = students_count
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) <= self.students_count:
            self.students.append(name)
            self.grades.append(grade)


    def get_average_grade(self):
        self.average_grade = sum(self.grades) / len(self.students)
        return self.average_grade

    def __repr__(self):
        return f"The students in {self.class_name}: {', '.join(self.students)}. Average grade: {self.average_grade:.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
# a_class.add_student("Peter1", 4.80)
# a_class.add_student("George1", 6.00)
# a_class.add_student("Amy1", 3.50)
# a_class.add_student("Peter2", 4.80)
# a_class.add_student("George2", 6.00)
# a_class.add_student("Amy2", 3.50)
# a_class.add_student("Peter3", 4.80)
# a_class.add_student("George3", 6.00)
# a_class.add_student("Amy3", 3.50)
# a_class.add_student("Peter4", 4.80)
# a_class.add_student("George4", 6.00)
# a_class.add_student("Amy4", 3.50)
# a_class.add_student("Peter5", 4.80)
# a_class.add_student("George5", 6.00)
# a_class.add_student("Amy5", 3.50)
# a_class.add_student("Peter6", 4.80)
# a_class.add_student("George6", 6.00)
# a_class.add_student("Amy6", 3.50)
# a_class.add_student("Peter7", 4.80)
# a_class.add_student("George7", 6.00)
# a_class.add_student("Amy7", 3.50)
# a_class.add_student("Peter8", 4.80)
# a_class.add_student("George8", 6.00)
# a_class.add_student("Amy8", 3.50)
print(a_class)

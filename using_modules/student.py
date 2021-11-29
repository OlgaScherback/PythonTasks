import human


class Student(human.Human):
    def __init__(self, name, surname, age, phone_number, num_course):
        super().__init__(name, surname, age, phone_number)
        self.num_course = num_course

    def __str__(self):
        return super().__str__() + " num_course={}".format(self.num_course)

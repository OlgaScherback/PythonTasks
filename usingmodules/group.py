import exep


class Group:
    def __init__(self):
        self.list_students = []

    def add_student(self, student):
        try:
            self.list_students.append(student)
            if len(self.list_students) > 10:
                raise exep.TooManyStudents(len(self.list_students))
        except exep.TooManyStudents as err:
            print(err)

    def del_student(self, student):
        self.list_students.remove(student)

    def search_surname(self, surname):
        for student in self.list_students:
            if student.surname == surname:
                return student.__str__()

    def __str__(self):
        stud_str = ""
        for student in self.list_students:
            stud_str += student.__str__()
        return stud_str

import group
import student

student_1 = student.Student("Oleg", "Storchaka", "18", "50585085", "1")
student_2 = student.Student("Nadya", "Semchuk", "19", "0000089898", "2")

group_1 = group.Group()
group_1.add_student(student_1)
group_1.add_student(student_2)

for student in group_1:
    print(student)

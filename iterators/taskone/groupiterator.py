class GroupIterator:
    def __init__(self, list_students):
        self.list_students = list_students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list_students):
            raise StopIteration()
        temp_student = self.list_students[self.index]
        self.index += 1
        return temp_student

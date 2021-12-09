class TooManyStudents(Exception):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def __str__(self):
        return "You cannot add more than ten students"

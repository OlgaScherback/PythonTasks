class Human():
    def __init__(self, name, surname, age, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return " name={}, surname={}, age={}, phone_number={}".format(self.name, self.surname, self.age,
                                                                      self.phone_number)
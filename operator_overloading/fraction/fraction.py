import exept


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        if self.numerator < self.denominator and other.numerator < other.denominator:
            return self.numerator / self.denominator == other.numerator / other.denominator
        else:
            try:
                raise exept.WrongFraction(self.numerator, self.denominator)
            except exept.WrongFraction as err:
                print(err)

    def __gt__(self, other):
        if self.numerator < self.denominator and other.numerator < other.denominator:
            return self.numerator / self.denominator > other.numerator / other.denominator
        else:
            try:
                raise exept.WrongFraction(self.numerator, self.denominator)
            except exept.WrongFraction as err:
                print(err)

    def __add__(self, other):
        if self.numerator < self.denominator and other.numerator < other.denominator:
            return self.numerator / self.denominator == other.numerator / other.denominator
        else:
            try:
                raise exept.WrongFraction(self.numerator, self.denominator)
            except exept.WrongFraction as err:
                print(err)

    def __sub__(self, other):
        if self.numerator < self.denominator and other.numerator < other.denominator:
            return self.numerator / self.denominator - other.numerator / other.denominator
        else:
            try:
                raise exept.WrongFraction(self.numerator, self.denominator)
            except exept.WrongFraction as err:
                print(err)

    def __mul__(self, other):
        if self.numerator < self.denominator and other.numerator < other.denominator:
            return self.numerator / self.denominator * other.numerator / other.denominator
        else:
            try:
                raise exept.WrongFraction(self.numerator, self.denominator)
            except exept.WrongFraction as err:
                print(err)


fraction_1 = Fraction(1, 3)
fraction_2 = Fraction(1, 2)

print(fraction_1 == fraction_2)
print(fraction_1 < fraction_2)
print(fraction_1 + fraction_2)
print(fraction_1 - fraction_2)
print(fraction_1 * fraction_2)

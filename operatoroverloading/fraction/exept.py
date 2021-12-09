class WrongFraction(Exception):
    def __init__(self, numerator, denominator):
        super().__init__()
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "Enter a correct fraction so that the numerator is less than the denominator."

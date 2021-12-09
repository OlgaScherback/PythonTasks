class Product:
    def __init__(self, name, price, desc, dimension):
        self.name = name
        self.price = price
        self.desc = desc
        self.dimension = dimension

    def __str__(self):
        return "Product [name = {}, price = {}, desc = {}, dimension = {}]".format(self.name, self.price, self.desc,
                                                                                   self.dimension)
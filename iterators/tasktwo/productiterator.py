class ProductIterator:
    def __init__(self, products_list):
        self.products_list = products_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.products_list):
            raise StopIteration()
        temp_product = self.products_list[self.index]
        self.index += 1
        return temp_product

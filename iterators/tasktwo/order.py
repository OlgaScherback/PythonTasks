import productiterator


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products_list = []
        self.prices_list = []

    def add_product(self, product):
        self.products_list.append(product)
        self.prices_list.append(product.price)

    def sum_order(self):
        summa = 0
        for price in self.prices_list:
            summa += price
        return summa

    def __str__(self):
        result = "Order ["
        for product in self.products_list:
            result += str(product) + " "
        result += "]"
        return result

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.products_list):
                return self.products_list[index]
            else:
                raise IndexError()

        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.products_list) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            temp_product_list = []
            if start < 0 and stop >= len(self.products_list):
                raise IndexError()
            for i in range(start, stop, step):
                temp_product_list.append(self.products_list[i])
            return temp_product_list

        raise TypeError

    def __len__(self):
        return len(self.products_list)

    def __iter__(self):
        return productiterator.ProductIterator(self.products_list)
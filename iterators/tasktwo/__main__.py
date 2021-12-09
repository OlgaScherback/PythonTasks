import customer
import order
import product


customer = customer.Customer("Alina", "Schevchenko", "05058958949")
order = order.Order(customer)

product_one = product.Product("Яблоко", 25, "Голден", "10х15")
product_two = product.Product("Груша", 30, "Зеленая", "10х15")

order.add_product(product_one)
order.add_product(product_two)

print(order)
print(order.customer)
print(order.sum_order())
print(order[0])
print(order[1])
print(len(order))

for product in order:
    print(product)
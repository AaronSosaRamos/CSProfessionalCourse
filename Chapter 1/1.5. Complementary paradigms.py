# Functional Paradigm
def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply_function(func, x):
    return func(x)

# Procedural Paradigm
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Declarative Paradigm
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        return sum(item.price for item in self.items)


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == "__main__":
    # Functional Paradigm
    print("Functional Paradigm:")
    print("Square of 5:", apply_function(square, 5))
    print("Cube of 5:", apply_function(cube, 5))
    print()

    # Procedural Paradigm
    print("Procedural Paradigm:")
    print("Factorial of 5:", calculate_factorial(5))
    print()

    # Declarative Paradigm
    print("Declarative Paradigm:")
    cart = ShoppingCart()
    cart.add_item(Item("Shirt", 20))
    cart.add_item(Item("Pants", 30))
    cart.add_item(Item("Shoes", 50))
    print("Total Price:", cart.total_price())

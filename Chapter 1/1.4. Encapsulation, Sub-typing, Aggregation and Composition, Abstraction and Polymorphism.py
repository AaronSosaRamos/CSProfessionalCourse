# Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Encapsulated field
        self._balance = balance  # Encapsulated field

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")


# Sub-typing
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Aggregation and Composition
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Aggregation


class Computer:
    def __init__(self):
        self.cpu = CPU()  # Composition


class CPU:
    pass


# Abstraction
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# Polymorphism
def get_area(shape):
    return shape.area()


if __name__ == "__main__":
    # Encapsulation
    account = BankAccount("12345", 1000)
    account.withdraw(500)
    print("Remaining balance:", account._balance)

    # Sub-typing
    dog = Dog()
    cat = Cat()
    print("Dog says:", dog.speak())
    print("Cat says:", cat.speak())

    # Aggregation and Composition
    engine = Engine(200)
    car = Car("Toyota", "Camry", engine)
    print("Car make:", car.make)
    print("Car engine horsepower:", car.engine.horsepower)

    # Abstraction
    rectangle = Rectangle(5, 4)
    circle = Circle(3)
    print("Rectangle area:", rectangle.area())
    print("Circle area:", circle.area())

    # Polymorphism
    shapes = [rectangle, circle]
    for shape in shapes:
        print("Area:", get_area(shape))

# Parametric polymorphism with type hinting

# Parametric polymorphism, also known as generic polymorphism, allows functions and classes to operate with generic types. 
# In Python, this is commonly achieved using type hints or through built-in generic types in modules like typing.

from typing import TypeVar

T = TypeVar('T')

def identity(x: T) -> T:
    return x

print(identity(5))  # Output: 5
print(identity("Hello"))  # Output: Hello

# Inclusion polymorphism with method overriding

# Inclusion polymorphism, also known as subtype polymorphism or runtime polymorphism, allows objects of different classes to be treated as 
# objects of a common superclass. This is achieved through method overriding.

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

def make_sound(animal):
    return animal.sound()

dog = Dog()
print(make_sound(dog))  # Output: Woof!

cat = Cat()
print(make_sound(cat))  # Output: Meow!

# Inheritance of types with method override

#Type inheritance with method override allows subclasses to provide a specific implementation of a method defined in their superclass.

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Override
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):  # Override
        return self.length * self.width

circle = Circle(5)
print(circle.area())  # Output: 78.5

rectangle = Rectangle(4, 6)
print(rectangle.area())  # Output: 24

# Association (6.1)

# Association is a relationship where two or more classes are connected or associated with each other, but they are not dependent on each other. 
# Each class remains independent.

class Car:
    def __init__(self, model):
        self.model = model

class Person:
    def __init__(self, name):
        self.name = name

    def drive(self, car):
        print(f"{self.name} is driving {car.model}")

car = Car("Toyota")
person = Person("John")
person.drive(car)  # Output: John is driving Toyota

# Composition (6.2)

# Composition is a relationship where one class (container) contains another class (component), and the component cannot 
# exist without the container. If the container is destroyed, all its components are also destroyed.


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine(200)  # Engine is composed inside Car

car = Car("Toyota")
print(car.engine.horsepower)  # Output: 200

# Aggregation (6.3)

# Aggregation is a relationship where one class (container) contains another class (component), but the component can exist 
# independently of the container. If the container is destroyed, the component still exists.


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

student1 = Student("John", 1)
student2 = Student("Alice", 2)

course = Course("Math")
course.add_student(student1)
course.add_student(student2)

print(course.students[0].name)  # Output: John

# Inheritance (Virtual Functions) (6.4)

# Inheritance is a mechanism where a new class (subclass) is derived from an existing class (superclass). The subclass inherits attributes 
# and methods from the superclass.

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog()
print(dog.sound())  # Output: Woof!

cat = Cat()
print(cat.sound())  # Output: Meow!

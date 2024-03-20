class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class FriendFunction:
    @staticmethod
    def add_person_age(person, years):
        person.age += years


class MyClass:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

    def some_function(self):
        print("Some function called")


if __name__ == "__main__":
    # Constructor and Destructor
    obj1 = MyClass()
    obj1.some_function()
    del obj1

    # Fields and Methods
    person1 = Person("Alice", 30)
    person1.display()

    rectangle = Rectangle(5, 4)
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())

    # Friend Function
    friend_function = FriendFunction()
    friend_function.add_person_age(person1, 5)
    print("New Age:", person1.age)

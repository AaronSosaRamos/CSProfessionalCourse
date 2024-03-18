# 8. Operator Overloading

# 8.1 Friend Functions

# Friend functions in C++ allow a function to access the private and protected members of a class. In Python, since there are no access 
# specifiers like private and protected, all methods and attributes are accessible from outside the class. However, you can achieve 
# similar behavior by defining helper functions or using decorators.

class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass: {self.value}"

# Helper function
def multiply(obj, factor):
    return obj.value * factor

obj = MyClass(5)
result = multiply(obj, 3)
print(result)  # Output: 15

# 8.2 Operator Overloading

# Operator overloading in Python allows you to define custom behavior for operators such as +, -, *, /, etc., 
# for your custom classes by implementing special methods.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading addition operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overloading string representation
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: (4, 6)

# 8.3 Special Cases of Operator Overloading

# There are specific cases of operator overloading such as __eq__, __lt__, __gt__, etc., for implementing equality, 
# comparison, and other specific behaviors.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading equality operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Overloading less than operator
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)  # Output: True
print(p1 < p3)   # Output: True

# 9. Templates and Files

# 9.1 Template Definitions
# Generic function

# In Python, the equivalent of templates in C++ are typically achieved using generic programming or 
# simply by defining functions that accept generic types.

def add(a, b):
    return a + b

print(add(5, 3))      # Output: 8
print(add("hello", "world"))  # Output: helloworld

# 9.2 Files: Definitions and Usage Modes

# Working with files in Python is straightforward. You can use built-in functions like open() to work with files in 
# different modes (read, write, append, etc.).

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.")

# Reading from a file
with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)

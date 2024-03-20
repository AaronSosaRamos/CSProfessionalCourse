# Duck Typing: Python follows the principle of "duck typing," which means objects are defined by their 
# behavior rather than their type. Here's an example:

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(obj):
    obj.quack()

duck = Duck()
person = Person()

make_it_quack(duck)    # Output: Quack!
make_it_quack(person)  # Output: I'm quacking like a duck!

# Type Hints: Python 3.5 introduced type hints, allowing developers to specify the expected types of variables, 
# function arguments, and return values. However, these hints are not enforced at runtime by Python itself.

def greet(name: str) -> str:
    return f"Hello, {name}"

print(greet("Alice"))  # Output: Hello, Alice

# Static Typing with External Tools: Although Python itself does not enforce type hints at runtime, 
# you can use external tools like MyPy to statically analyze your code and catch type errors.

def add(x: int, y: int) -> int:
    return x + y

result = add(5, "10")  # MyPy will raise a type error here

#Type Aliases: Python allows you to define aliases for complex types, improving code readability.

from typing import List, Tuple

Vector = List[float]
Point = Tuple[float, float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

def translate(point: Point, vector: Vector) -> Point:
    return (point[0] + vector[0], point[1] + vector[1])
# Namespace
class Namespace:
    def __init__(self, name):
        self.name = name
        self.variables = {}

    def add_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        return self.variables.get(name, None)


# Libraries
class MathLibrary:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b


class StringLibrary:
    @staticmethod
    def concatenate(a, b):
        return str(a) + str(b)


# Operator Overloading
class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value + other.value)
        elif isinstance(other, int) or isinstance(other, float):
            return MyNumber(self.value + other)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'MyNumber' and '{}'".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value - other.value)
        elif isinstance(other, int) or isinstance(other, float):
            return MyNumber(self.value - other)
        else:
            raise TypeError("Unsupported operand type(s) for -: 'MyNumber' and '{}'".format(type(other)))


if __name__ == "__main__":
    # Namespace
    global_namespace = Namespace("Global")
    global_namespace.add_variable("x", 10)
    global_namespace.add_variable("y", 20)

    # Libraries
    math = MathLibrary()
    string = StringLibrary()

    # Operator Overloading
    num1 = MyNumber(5)
    num2 = MyNumber(3)
    result_add = num1 + num2
    result_sub = num1 - num2

    print("Namespace Variables:")
    print(global_namespace.variables)
    print()

    print("Math Library:")
    print("Addition:", math.add(10, 5))
    print("Subtraction:", math.subtract(10, 5))
    print()

    print("String Library:")
    print("Concatenation:", string.concatenate("Hello ", "World"))
    print()

    print("Operator Overloading:")
    print("Addition:", result_add.value)
    print("Subtraction:", result_sub.value)

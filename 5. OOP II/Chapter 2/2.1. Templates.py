# Class template
class MyGenericClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print("Generic value:", self.value)


# Function template
def generic_function(value):
    print("Generic value:", value)


# Variadic template function
def variadic_function(*args):
    print("Variadic arguments:", args)


# Template specialization
class SpecializedClass(MyGenericClass):
    def display(self):
        print("Specialized value:", self.value)


def main():
    # Instantiating generic class
    generic_obj = MyGenericClass(10)
    generic_obj.display()

    # Calling generic function
    generic_function("Hello")

    # Calling variadic function with different number of arguments
    variadic_function(1, 2, 3)
    variadic_function('a', 'b', 'c', 'd')

    # Using specialized class
    specialized_obj = SpecializedClass(20)
    specialized_obj.display()


if __name__ == "__main__":
    main()

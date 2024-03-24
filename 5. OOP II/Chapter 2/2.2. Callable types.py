# Lambda function
lambda_function = lambda x: x * 2

# Function object
class MyFunctionObject:
    def __call__(self, x):
        return x * 3

# Function pointer
def function_pointer(x):
    return x * 4

# Functor
class MyFunctor:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, x):
        return x * self.multiplier

def main():
    # Using lambda function
    result_lambda = lambda_function(5)
    print("Lambda function result:", result_lambda)

    # Using function object
    function_object = MyFunctionObject()
    result_function_object = function_object(5)
    print("Function object result:", result_function_object)

    # Using function pointer
    result_function_pointer = function_pointer(5)
    print("Function pointer result:", result_function_pointer)

    # Using functor
    my_functor = MyFunctor(5)
    result_functor = my_functor(5)
    print("Functor result:", result_functor)

if __name__ == "__main__":
    main()

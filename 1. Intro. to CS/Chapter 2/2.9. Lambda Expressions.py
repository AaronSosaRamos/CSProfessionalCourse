# Lambda function to calculate the sum of two numbers
add = lambda x, y: x + y

# Lambda function to calculate the product of two numbers
multiply = lambda x, y: x * y

# Example usage of lambda functions
print(add(2, 3))        # Output: 5
print(multiply(2, 3))   # Output: 6

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using lambda function with map() to double each number in the list
doubled = list(map(lambda x: x * 2, numbers))

# Using lambda function with filter() to filter out even numbers
filtered = list(filter(lambda x: x % 2 == 0, numbers))

# Example usage of map() and filter() with lambda functions
print(doubled)   # Output: [2, 4, 6, 8, 10]
print(filtered)  # Output: [2, 4]

# Higher-order function that applies a given operation to two numbers
def apply_operation(x, y, operation):
    return operation(x, y)

# Example usage of apply_operation with a lambda function
result = apply_operation(4, 5, lambda a, b: a + b)
print(result)  # Output: 9

# Lambda function demonstrating closure by capturing a variable from the enclosing scope
def make_incrementer(n):
    # Returns a lambda function that increments its argument by n
    return lambda x: x + n

# Create a function that increments by 42
f = make_incrementer(42)

# Example usage of the closure
print(f(0))  # Output: 42

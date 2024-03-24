# Asymptotic Upper Bound and Big O Notation in Python

# Example function to analyze
def example_function(n):
    """
    Example function to analyze its time complexity.
    This function has a quadratic time complexity O(n^2).
    """
    result = 0
    for i in range(n):
        for j in range(n):
            result += i * j
    return result

# Example usage
if __name__ == "__main__":
    # Define the input size
    input_size = 10

    # Call the example function
    result = example_function(input_size)

    # Print the result
    print("Result:", result)

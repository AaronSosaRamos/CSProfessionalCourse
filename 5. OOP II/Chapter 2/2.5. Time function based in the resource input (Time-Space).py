import time
import random
import sys

# Function to demonstrate an algorithm to analyze
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

# Function to generate random data for testing
def generate_random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Function to perform empirical analysis
def empirical_analysis(algorithm, data_size, resource='time'):
    data = generate_random_data(data_size)
    
    if resource == 'time':
        # Measure execution time
        start_time = time.time()
        algorithm(data, random.choice(data))
        end_time = time.time()
        measurement = end_time - start_time
    elif resource == 'space':
        # Measure space complexity
        measurement = sys.getsizeof(data)
    else:
        raise ValueError("Invalid resource. Choose 'time' or 'space'.")
    
    return measurement

# Perform empirical analysis for different data sizes and resources
data_sizes = [1000, 5000, 10000]
resources = ['time', 'space']

for size in data_sizes:
    for resource in resources:
        result = empirical_analysis(linear_search, size, resource)
        print(f"Analysis for data size {size} and resource {resource}: {result}")

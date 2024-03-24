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
def empirical_analysis(algorithm, data_size):
    data = generate_random_data(data_size)
    
    # Measure execution time
    start_time = time.time()
    algorithm(data, random.choice(data))
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Measure space complexity
    data_size_bytes = sys.getsizeof(data)
    
    # Measure scalability
    scalability = execution_time / data_size
    
    # Check stability
    sorted_data = sorted(data)
    stability = all(data[i] <= data[i+1] for i in range(len(data)-1))
    
    print(f"Analysis for data size {data_size}:")
    print(f"  - Execution time: {execution_time:.6f} seconds")
    print(f"  - Space complexity: {data_size_bytes} bytes")
    print(f"  - Scalability: {scalability:.6f} seconds per element")
    print(f"  - Stability: {'Stable' if stability else 'Unstable'}")
    print()

# Perform empirical analysis for different data sizes
data_sizes = [1000, 5000, 10000]
for size in data_sizes:
    empirical_analysis(linear_search, size)

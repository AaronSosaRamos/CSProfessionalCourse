import time

def algorithm_example(arr):
    """
    Example algorithm to demonstrate best, average, and worst-case scenarios.
    This algorithm sorts a given array in ascending order using bubble sort.
    """

    # Best case: Array is already sorted
    is_sorted = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_sorted = False
            break
    if is_sorted:
        return arr

    # Worst case: Array is sorted in descending order
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Test cases
best_case = [1, 2, 3, 4, 5]  # Best case: Ω(n)
average_case = [5, 3, 1, 4, 2]  # Average case: Θ(n^2)
worst_case = [5, 4, 3, 2, 1]  # Worst case: O(n^2)

# Measure time for best case
start_time = time.time()
algorithm_example(best_case)
best_case_time = time.time() - start_time

# Measure time for average case
start_time = time.time()
algorithm_example(average_case)
average_case_time = time.time() - start_time

# Measure time for worst case
start_time = time.time()
algorithm_example(worst_case)
worst_case_time = time.time() - start_time

print("Best Case Time:", best_case_time)
print("Average Case Time:", average_case_time)
print("Worst Case Time:", worst_case_time)

print("Best Case (Ω(n)):", algorithm_example(best_case))
print("Average Case (Θ(n^2)):", algorithm_example(average_case))
print("Worst Case (O(n^2)):", algorithm_example(worst_case))
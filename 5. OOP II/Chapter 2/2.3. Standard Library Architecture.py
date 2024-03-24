# Importing necessary modules from the standard library
import itertools  # Module for efficient looping
import collections  # Module for specialized container datatypes
import functools  # Module for higher-order functions and operations
import operator  # Module providing a set of efficient functions for common operations
import random  # Module for generating random numbers
import math  # Module providing mathematical functions

# Containers: Lists, Tuples, Sets, Dictionaries
my_list = [1, 2, 3, 4, 5]  # List
my_tuple = (1, 2, 3, 4, 5)  # Tuple
my_set = {1, 2, 3, 4, 5}  # Set
my_dict = {'a': 1, 'b': 2, 'c': 3}  # Dictionary

# Iterators: range, enumerate, zip
for i in range(5):  # range is an iterator generating arithmetic progressions
    print(i)

for index, value in enumerate(my_list):  # enumerate returns an iterator of tuples containing indices and values
    print(index, value)

for pair in zip(my_list, my_tuple):  # zip returns an iterator of tuples combining elements from multiple iterables
    print(pair)

# Algorithms: Sorting, Filtering, Mapping
sorted_list = sorted(my_list)  # Sorting algorithm
filtered_list = filter(lambda x: x % 2 == 0, my_list)  # Filtering algorithm using a lambda function
mapped_list = map(lambda x: x * 2, my_list)  # Mapping algorithm using a lambda function

# Callable: Functions, Lambdas, Functors
def my_function(x):
    return x ** 2

my_lambda = lambda x: x ** 2

class MyFunctor:
    def __call__(self, x):
        return x ** 2

my_functor = MyFunctor()

# Using functions, lambdas, and functors
print(my_function(3))
print(my_lambda(3))
print(my_functor(3))

# Other standard library modules for various tasks
# - os: Operating system interfaces
# - sys: System-specific parameters and functions
# - datetime: Basic date and time types
# - json: JSON encoder and decoder
# - re: Regular expression operations
# - urllib: URL handling modules
# - and many more...


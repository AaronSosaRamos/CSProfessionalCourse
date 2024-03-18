import ctypes
import array

# Simulating pointer behavior
a = [1, 2, 3]
b = a  # 'b' now points to the same list as 'a'
b[0] = 5  # Modifying 'b' will also change 'a'
print(a)  # Output: [5, 2, 3]

# Memory Management
size = 5
arr_type = ctypes.c_int * size
arr = arr_type()

# Writing to memory
for i in range(size):
    arr[i] = i

# Accessing memory
print("Memory contents:")
for i in range(size):
    print(arr[i])

# Freeing memory (not necessary in Python)
del arr

# Dynamic Arrays
# Using Python lists
dynamic_array = []
dynamic_array.append(1)
dynamic_array.append(2)
dynamic_array.append(3)
print("Dynamic array using Python lists:", dynamic_array)  # Output: [1, 2, 3]

# Using array module for more efficient storage
dynamic_array = array.array('i')  # 'i' for integer type
dynamic_array.append(1)
dynamic_array.append(2)
dynamic_array.append(3)
print("Dynamic array using array module:", dynamic_array)  # Output: array('i', [1, 2, 3])

# typedef struct {
#     PyObject_VAR_HEAD
#     PyObject **ob_item;  // Pointer to an array of PyObject pointers
#     Py_ssize_t allocated;  // Allocated size of the list
# } PyListObject;

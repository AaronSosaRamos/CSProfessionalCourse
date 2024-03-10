import os  # This module provides a portable way of using operating system dependent functionality. It mainly deals with file and directory operations, process management, and environment variables.
import sys  # The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. It's often used for system-specific parameters and functions.
import subprocess  # This module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. It's a powerful tool for interacting with other programs and the system shell.
import shutil  # The shutil module offers a number of high-level operations on files and collections of files. It is especially useful for copying, moving, and deleting files and directories.
import tempfile  # This module generates temporary files and directories. It simplifies the process of creating and handling temporary files and directories, which can be useful for various tasks.
import multiprocessing  # This module allows the creation of processes using an API similar to threading. It offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads.

# Example using 'os' module
print("--- os module ---")

# File and directory operations
print("Current Working Directory:", os.getcwd())

# Process management
pid = os.getpid()
print("Current Process ID:", pid)

# Environment variables
print("Value of HOME environment variable:", os.environ.get('HOME'))

# Example using 'sys' module
print("\n--- sys module ---")

# System-specific parameters
print("Python Version:", sys.version)
print("Python Executable Path:", sys.executable)

# Example using 'tempfile' module
print("\n--- tempfile module ---")

# Creating temporary files
with tempfile.NamedTemporaryFile() as tmpfile:
    print("Temporary File Created:", tmpfile.name)

# Example using 'os.path' module
print("\n--- os.path module ---")

# Joining paths
print("Joined Path:", os.path.join("/path/to", "file.txt"))

# Example using 'multiprocessing' module
print("\n--- multiprocessing module ---")

# Local concurrency
def square(x):
    return x * x

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        result = pool.map(square, [1, 2, 3, 4, 5])
        print("Result of multiprocessing Pool:", result)

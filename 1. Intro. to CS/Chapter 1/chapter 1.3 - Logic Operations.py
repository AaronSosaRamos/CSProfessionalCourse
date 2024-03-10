# Logic table for AND operation
print("AND Logic Table:")
print("A\tB\tResult")
print("-"*20)
for A in [True, False]:
    for B in [True, False]:
        result = A and B
        print(f"{A}\t{B}\t{result}")

# Logic table for OR operation
print("\nOR Logic Table:")
print("A\tB\tResult")
print("-"*20)
for A in [True, False]:
    for B in [True, False]:
        result = A or B
        print(f"{A}\t{B}\t{result}")

# Logic table for XOR operation
print("\nXOR Logic Table:")
print("A\tB\tResult")
print("-"*20)
for A in [True, False]:
    for B in [True, False]:
        result = A ^ B
        print(f"{A}\t{B}\t{result}")

# Logic table for NOT operation
print("\nNOT Logic Table:")
print("A\tResult")
print("-"*20)
for A in [True, False]:
    result = not A
    print(f"{A}\t{result}")

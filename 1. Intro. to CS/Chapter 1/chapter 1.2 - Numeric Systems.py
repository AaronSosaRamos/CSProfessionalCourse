# Decimal: The standard base-10 system used in everyday arithmetic.
decimal_number = 10

# Binary: Base-2 system consisting of only 0s and 1s.
binary_number = 0b1010  # This represents 10 in decimal

# Octal: Base-8 system using digits from 0 to 7.
octal_number = 0o12  # This represents 10 in decimal

# Hexadecimal: Base-16 system using digits from 0 to 9 and letters from A to F.
hexadecimal_number = 0xA  # This represents 10 in decimal

# Convert decimal to binary, octal, and hexadecimal
binary_representation = bin(decimal_number)
octal_representation = oct(decimal_number)
hexadecimal_representation = hex(decimal_number)

# Print representations
print("Decimal:", decimal_number)
print("Binary:", binary_representation)  # Prints '0b1010'
print("Octal:", octal_representation)    # Prints '0o12'
print("Hexadecimal:", hexadecimal_representation)  # Prints '0xa'

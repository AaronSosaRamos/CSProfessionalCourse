# AND Gate: Produces a true output only if both inputs are true.
def AND_gate(input1, input2):
    return input1 and input2

# Example:
# Both conditions need to be True for the output to be True.
result = AND_gate(True, False)
print(result)  # Output: False

# OR Gate: Produces a true output if at least one input is true.
def OR_gate(input1, input2):
    return input1 or input2

# Example:
# At least one condition needs to be True for the output to be True.
result = OR_gate(True, False)
print(result)  # Output: True

# NOT Gate: Inverts the input.
def NOT_gate(input):
    return not input

# Example:
# Inverts the input value.
result = NOT_gate(True)
print(result)  # Output: False

# NAND Gate: Produces the opposite result of an AND gate.
def NAND_gate(input1, input2):
    return not (input1 and input2)

# Example:
# Opposite result of an AND gate.
result = NAND_gate(True, False)
print(result)  # Output: True

# NOR Gate: Produces the opposite result of an OR gate.
def NOR_gate(input1, input2):
    return not (input1 or input2)

# Example:
# Opposite result of an OR gate.
result = NOR_gate(True, False)
print(result)  # Output: False

# XOR Gate: Produces a true output if exactly one input is true.
def XOR_gate(input1, input2):
    return (input1 and not input2) or (not input1 and input2)

# Example:
# True output if exactly one input is True.
result = XOR_gate(True, False)
print(result)  # Output: True

# Function to simulate a security system
def security_system(door_sensor, motion_sensor, password_correct, fingerprint_authenticated):
    # Use AND gate to ensure both sensors are triggered
    motion_and_door = AND_gate(door_sensor, motion_sensor)

    # Use NAND gate to ensure the password and fingerprint are both correct
    authentication = AND_gate(password_correct, fingerprint_authenticated)

    # Use OR gate to allow access if either sensors are triggered or authentication is successful
    access_granted = OR_gate(motion_and_door, authentication)

    return access_granted

# Simulating the security system with example inputs
door_sensor = True
motion_sensor = True
password_correct = True
fingerprint_authenticated = True

# Check if access is granted
result = security_system(door_sensor, motion_sensor, password_correct, fingerprint_authenticated)
print("Access Granted:", result)  # Output: Access Granted: True
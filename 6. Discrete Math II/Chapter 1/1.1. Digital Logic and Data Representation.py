#1.1. Partially Ordered Set
#1.1.1. Hasse Diagrams

# Partially Ordered Set (Poset) and Hasse Diagram

# Define a partial order relation
partial_order = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': []
}

# Function to generate Hasse diagram
def generate_hasse_diagram(partial_order):
    edges = []
    for element, successors in partial_order.items():
        for successor in successors:
            edges.append((element, successor))

    return edges

# Example of Hasse diagram generation
print("Hasse Diagram:")
print(generate_hasse_diagram(partial_order))

#1.2. Lattice
#1.2.1. Types and Properties
# Lattice

class Lattice:
    def __init__(self, elements, join, meet):
        self.elements = elements
        self.join = join  # Function to compute join (supremum)
        self.meet = meet  # Function to compute meet (infimum)

    def compute_join(self, a, b):
        return self.join(a, b)

    def compute_meet(self, a, b):
        return self.meet(a, b)

# Example of creating a lattice for integers with operations max and min
integers_lattice = Lattice(
    elements=[0, 1, 2, 3],
    join=max,
    meet=min
)

# Example of using lattice operations
print("Join of 2 and 3:", integers_lattice.compute_join(2, 3))
print("Meet of 2 and 3:", integers_lattice.compute_meet(2, 3))

#1.3. Boolean Algebras
# Boolean Algebra

class BooleanAlgebra:
    def __init__(self, elements, conjunction, disjunction, negation):
        self.elements = elements
        self.conjunction = conjunction
        self.disjunction = disjunction
        self.negation = negation

    def compute_conjunction(self, a, b):
        return self.conjunction(a, b)

    def compute_disjunction(self, a, b):
        return self.disjunction(a, b)

    def compute_negation(self, a):
        return self.negation(a)

# Example of creating a boolean algebra for {False, True} with operations AND, OR, NOT
boolean_algebra = BooleanAlgebra(
    elements=[False, True],
    conjunction=lambda a, b: a and b,
    disjunction=lambda a, b: a or b,
    negation=lambda a: not a
)

# Example of using boolean algebra operations
print("Conjunction of True and False:", boolean_algebra.compute_conjunction(True, False))
print("Disjunction of True and False:", boolean_algebra.compute_disjunction(True, False))
print("Negation of True:", boolean_algebra.compute_negation(True))

#1.4. Boolean Functions and Expressions
#1.4.1. Disjunctive Normal Form and Conjunctive Normal Form
# Boolean Functions and Normal Forms

# Define a Boolean function
def boolean_function(a, b, c):
    return (not a and not b) or (a and not b) or (b and c)

# Disjunctive Normal Form (DNF)
def dnf(boolean_function):
    terms = []
    for assignment in [(a, b, c) for a in [False, True] for b in [False, True] for c in [False, True]]:
        if boolean_function(*assignment):
            terms.append("({}{}{})".format("" if assignment[0] else "¬", "a" if assignment[0] else "¬a",
                                           "" if assignment[1] else "¬" + "b" if assignment[1] else "¬b",
                                           "" if assignment[2] else "¬" + "c" if assignment[2] else "¬c"))
    return " + ".join(terms)

# Conjunctive Normal Form (CNF)
def cnf(boolean_function):
    terms = []
    for assignment in [(a, b, c) for a in [False, True] for b in [False, True] for c in [False, True]]:
        if not boolean_function(*assignment):
            terms.append("({}{}{})".format("" if not assignment[0] else "¬", "a" if not assignment[0] else "¬a",
                                            "" if not assignment[1] else "¬" + "b" if not assignment[1] else "¬b",
                                            "" if not assignment[2] else "¬" + "c" if not assignment[2] else "¬c"))
    return " * ".join(terms)

# Example of using DNF and CNF
print("DNF:", dnf(boolean_function))
print("CNF:", cnf(boolean_function))

#1.4.2. Representation of Boolean Functions: Logic Circuits
# Logical Circuits

class LogicalCircuit:
    def __init__(self, gates):
        self.gates = gates

    def evaluate(self, inputs):
        outputs = {}
        for gate, connections in self.gates.items():
            if gate not in outputs:
                outputs[gate] = self.evaluate_gate(gate, inputs, outputs, connections)
        return outputs

    def evaluate_gate(self, gate, inputs, outputs, connections):
        values = []
        for connection in connections:
            if connection in inputs:
                # If the connection is an input, append its value directly
                values.append(inputs[connection])
            else:
                # Otherwise, get the value from the outputs dictionary
                values.append(outputs[connection])

        if gate == 'AND':
            return all(values)
        elif gate == 'OR':
            return any(values)
        elif gate == 'NOT':
            return not values[0]


# Example of logical circuit evaluation
circuit = LogicalCircuit({
    'AND': ['A', 'B'],
    'OR': ['C', 'D'],
    'NOT': ['E']
})

inputs = {'A': True, 'B': False, 'C': True, 'D': False, 'E': False}
print("Outputs:", circuit.evaluate(inputs))

#1.4.3. Minimal Sum of Products: Karnaugh Maps
# Karnaugh Maps
def truth_table_to_kmap(truth_table):
    """
    Convert truth table to a Karnaugh Map (K-map) representation.

    Args:
    - truth_table: A list of tuples representing the truth table, where each tuple is (input_values, output).

    Returns:
    - kmap: A dictionary representing the K-map.
    """
    num_inputs = len(truth_table[0][0])
    num_outputs = 1  # For simplicity, considering single output functions

    kmap = {}

    for input_values, output in truth_table:
        key = tuple(input_values)
        kmap[key] = output

    return kmap

def find_min_sop_from_kmap(kmap):
    """
    Find the minimal Sum of Products (SoP) expression from a Karnaugh Map (K-map).

    Args:
    - kmap: A dictionary representing the K-map.

    Returns:
    - min_sop: A string representing the minimal Sum of Products expression.
    """
    terms = []

    for inputs, output in kmap.items():
        if output == 1:
            term = []
            for i, value in enumerate(inputs):
                if value == 0:
                    term.append(f"~X{i}")
                elif value == 1:
                    term.append(f"X{i}")
            terms.append("".join(term))

    min_sop = " + ".join(terms)
    return min_sop

# Example truth table: (inputs, output)
truth_table = [
    ((0, 0), 0),
    ((0, 1), 1),
    ((1, 0), 1),
    ((1, 1), 0)
]

# Convert truth table to K-map
kmap = truth_table_to_kmap(truth_table)

# Find minimal Sum of Products expression
min_sop = find_min_sop_from_kmap(kmap)

print("Karnaugh Map:")
print(kmap)
print("\nMinimal Sum of Products expression:")
print(min_sop)

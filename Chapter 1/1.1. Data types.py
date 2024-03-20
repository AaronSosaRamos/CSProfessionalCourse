class DataType:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Data Type:", self.name)


class PrimitiveType(DataType):
    def __init__(self, name):
        super().__init__(name)


class CompositeType(DataType):
    def __init__(self, name, component_types):
        super().__init__(name)
        self.component_types = component_types

    def display_info(self):
        super().display_info()
        print("Component Types:", self.component_types)


class ReferenceType(DataType):
    def __init__(self, name, referenced_type):
        super().__init__(name)
        self.referenced_type = referenced_type

    def display_info(self):
        super().display_info()
        print("Referenced Type:", self.referenced_type.name)


if __name__ == "__main__":
    # Primitive Types
    int_type = PrimitiveType("int")
    float_type = PrimitiveType("float")
    bool_type = PrimitiveType("bool")
    str_type = PrimitiveType("str")

    # Composite Types
    list_type = CompositeType("list", [int_type])
    tuple_type = CompositeType("tuple", [int_type, float_type])
    dict_type = CompositeType("dict", [str_type, int_type])

    # Reference Types
    class_type = PrimitiveType("class")
    reference_list_type = ReferenceType("Reference to list", list_type)
    reference_dict_type = ReferenceType("Reference to dict", dict_type)

    # Displaying Information
    int_type.display_info()
    print()
    list_type.display_info()
    print()
    reference_list_type.display_info()

from abc import ABC, abstractmethod

class Person(ABC):  # 5.1 Abstraction Process
    def __init__(self, name, age):  # 5.4 Constructors
        self.name = name
        self.age = age
    
    @abstractmethod  # 5.5 Dynamic Objects
    def greet(self):
        pass

    def get_name(self):  # 5.3 Access Methods
        return self.name
    
    def set_name(self, new_name):  # 5.3 Modification Methods
        self.name = new_name
    
    def get_age(self):  # 5.3 Access Methods
        return self.age
    
    def set_age(self, new_age):  # 5.3 Modification Methods
        self.age = new_age
    
    def __del__(self):  # 5.4 Destructors
        print(f"{self.name} has been deleted.")

class Student(Person):  # 5.2 Class-Object Relationship
    def greet(self):  # Abstract Method Implementation
        print(f"Hello, I'm {self.name} and I'm {self.age} years old. I'm a student.")

class Teacher(Person):  # 5.2 Class-Object Relationship
    def greet(self):  # Abstract Method Implementation
        print(f"Hello, I'm {self.name} and I'm {self.age} years old. I'm a teacher.")

# Create dynamic objects
people = []  # 5.6 Arrays of Objects
people.append(Student("John", 20))
people.append(Teacher("Mary", 35))

# Access and modify attributes using getters and setters
print(people[0].get_name())  # Output: John
people[0].set_name("Peter")
print(people[0].get_name())  # Output: Peter

# Call methods
people[0].greet()  # Output: Hello, I'm Peter and I'm 20 years old. I'm a student.
people[1].greet()  # Output: Hello, I'm Mary and I'm 35 years old. I'm a teacher.

# Delete objects (calls destructor)
del people[0]  # Output: Peter has been deleted.
del people[0]  # Output: Mary has been deleted.

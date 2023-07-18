# Intro to Object-Oriented Programming

# Functional Programming vs. Object-Oriented Programming
# Functional -> we define and execute functions, pass anonymous functions
# Object-Oriented -> we use class/objects to solve fundamental problems

# Tuple
# - key/value pairs
# - tuples don't allow item assignment (IMMUTABLE)!!!!!
# - we can access a tuple via its INDEX

my_tuple = ("Harry", "Gryffindor")
name = my_tuple[0] # INDEX
house = my_tuple[1] # INDEX
print(name, house)

# List
# - collection of values
# - we can access a list via its INDEX
# - MUTABLE

my_list = ["Harry", "Gryffindor"]
name = my_list[0]
house = my_list[1]

# Dictionary
# - collection of keys/values
# - we can access a dictionary via its KEY
# - MUTABLE

my_dictionary = {
    "name": "Danny",
    "office": "Chicago",
}
name = my_dictionary["name"] # KEY
office = my_dictionary["office"] # KEY
print(name, office)

# Class
# - a blueprint to design objects as in Object-Oriented Programming
# - we can access a class' properties with "DOT" notation
# - class comes with default methods (__init__ & __str__)
# - class comes with custom methods (functions) that we can build ourselves

class Employee:
    def __init__(self, name, office):
        self.name = name
        self.office = office

    def __str__(self):
        return f"{self.name} from {self.office}"

    def greet(self):
        return f"Hello World! I'm {self.name}"

    # Getter:
    @property
    def name(self):
        return self._name

    # Setter:
    @name.setter
    def name(self, name):
        # error checking
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter:
    @property
    def office(self):
        return self._office

    # Setter:
    # - we can do error checking here automatically
    @office.setter
    def office(self, office):
        # error checking
        if office not in ["Google", "Apple", "Meta"]:
            raise ValueError("Invalid office")
        self._office = office

# employee = Employee()
# employee.name = "Danny"
# employee.office = "Chicago"

# print(employee.name) # Danny
# print(employee.office) # Chicago

# Properties
# - attribute with more self-defense mechanism

# Decorators
# - functions that modify behavior of other functions
# - we can define properties using decorators

# Getter
# - function that gets some attribute

# Setter
# - function that sets a value

# Why use Getter & Setter?
# - we can prevent programmers to maliciously set data that we carefully built
# - we will use error checking on "setter" automatically to validate attributes on a class
# - enable Python to automatically detect when programmers manually set a value on an attribute
# - HOWEVER; WHEN WE ASSIGN TO A HARDCODED VALUE IT WILL SLIP THROUGH...

def main():
    employee = get_employee()
    # HERE'S THE PROBLEM WITH GETTER/SETTER automatic ERROR CHECKS ALLOWING US TO "SET" AN ATTRIBUTE A DIFFERENT VALUE
    employee._office = "KPMG"
    print(employee) # allowed by __str__ default method of a class

# Connect Previous Work in Course
# - "int" is a class
# - "str" is a class
# - "list" is a class
# - "dict" is a class

# Methods are also part of the class
str.lower()
str.upper()
str.split(",")

# Check type of a specific data type?
print(type(50)) # int class
print(type("hello world")) # str class
print(type([])) # list class
print(type(list())) # list class
print(type({})) # dict class
print(type(dict())) # dict class

# Class Methods
# - add functionality to a class itself, not to "instances" of that class
# @classmethod -> function to add functionality to a class as a whole

import random
class Hat:
    # initialize houses as a list []
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    # classmethod -> function we can use to add functionality to a class as a whole
    @classmethod
    def sort(cls, name): # cls -> as class
        print(name, "is in", random.choice(cls.houses))
# no need to instantiate a class Object, we'll just sort on Hat class directly
Hat.sort("Harry") # Harry is in Ravenclaw

# Why bother with class methods?

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"This is a {self.model} from {self.make}"

    # classmethod of "GET"
    @classmethod
    def get(cls):
        make = input("Make: ")
        model = input("Model: ")
        return cls(make, model)

def main():
    # instantiate vehicle on class Vehicle
    vehicle = Vehicle.get()
    print(vehicle) # This is a CX5 from Mazda

if __name__ == "__main__":
    main()

# Static Methods
# - something to learn...

# Inheritance
# - most powerful feature of object-oriented programming
# - a class can "inherit" methods, variables and attributes from another class

class Wizard:
    def __init__(self, name):
        # error check
        if not name:
            raise ValueError("Missing name")
        self.name = name

# initialize a new class "INHERITING" from Wizard class
class Student(Wizard):
    def __init__(self, name, house):
        # "super" will extend from Wizard class
        super().__init__(name)
        self.house = house

# initialize a new class "INHERITING" from Wizard class
class Professor(Wizard):
    def __init__(self, name, subject):
        # "super" will extend from Wizard class
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

# Object Overloading...
# - some operators such as + and - can be “overloaded” such that they can have more abilities beyond simple arithmetic.

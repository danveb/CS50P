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


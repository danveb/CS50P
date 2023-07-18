class Employee:
    def __init__(self, name, office, club):
        # add properties
        self.name = name
        self.office = office
        self.club = club

    # __str__ method
    # - allows us to call employee() directly as string
    def __str__(self):
        return f"{self.name} from {self.office}"

    # custom method: function sport_type()
    def sport_type(self):
        match self.club:
            case "River Plate":
                return "soccer"
            case "River":
                return "soccer"
            case "Dodgers":
                return "baseball"
            case _:
                return "N/A"

    # custom method: function greet()
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

def main():
    employee = get_employee()
    # print("Welcome to CS50P")
    # HERE'S THE PROBLEM WITH GETTER/SETTER automatic ERROR CHECKS ALLOWING US TO "SET" AN ATTRIBUTE A DIFFERENT VALUE
    employee._office = "KPMG"
    print(employee)
    # print(employee.sport_type())
    # print(employee.greet())

def get_employee():
    name = input("Name: ")
    office = input("Office: ")
    club = input("Club: ")
    # return all attributes back to Employee class
    return Employee(name, office, club)

if __name__ == "__main__":
    main()
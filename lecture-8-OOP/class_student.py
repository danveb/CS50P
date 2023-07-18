# class Student:
#     ...

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     # instantiate Student class
#     student = Student()
#     # initialize student.name and student.house
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()

# Example 2
# class Student:
#     # init method
#     # - self parameter is a reference to the class instance and allows to access variables of the class
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
#     # object methods (functions)

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     # initialize name, house
#     name = input("Name: ")
#     house = input("House: ")
#     # instantiate Student with name, house properties built-in
#     student = Student(name, house)
#     return student

# if __name__ == "__main__":
#     main()

# Example 3
# class Student:
#     def __init__(self, name, house):
#         # error check: raise exceptions when something goes wrong
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#     # object methods (functions)

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     # initialize name, house
#     name = input("Name: ")
#     house = input("House: ")
#     # instantiate Student with name, house properties built-in
#     student = Student(name, house)
#     return student

# if __name__ == "__main__":
#     main()

# Example 4
# - validate attributes passed to __init__
# class Student:
#     def __init__(self, first, middle, last, house):
#         # error check: raise exceptions when something goes wrong
#         if not first:
#             raise ValueError("Missing first name")
#         if not middle:
#             raise ValueError("Missing middle name")
#         if not last:
#             raise ValueError("Missing last name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.first = first
#         self.middle = middle
#         self.last = last
#         self.house = house
#     # object methods (functions)

# def main():
#     student = get_student()
#     print(f"{student.first} {student.middle} {student.last} from {student.house}")

# def get_student():
#     # initialize name, house
#     first = input("First Name: ")
#     middle = input("Middle Name: ")
#     last = input("Last Name: ")
#     house = input("House: ")
#     # instantiate Student with name, house properties built-in
#     student = Student(first, middle, last, house)
#     return student

# if __name__ == "__main__":
#     main()

# Example 5
# class Student:
#     # pass a default value to house
#     def __init__(self, name, house=None):
#         # error check: raise exceptions when something goes wrong
#         if not name:
#             raise ValueError("Missing first name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#     # object methods (functions)

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     # initialize name, house
#     name = input("Name: ")
#     house = input("House: ")
#     # instantiate Student with name, house properties built-in
#     student = Student(name, house)
#     return student

# if __name__ == "__main__":
#     main()
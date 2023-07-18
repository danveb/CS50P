# Example 1
# name = input("Name: ")
# house = input("House: ")
# print(f"{name} from {house}")

# Example 2
# - implement helper functions to solve
# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")
# def get_name():
#     name = input("Name: ")
#     return name
# def get_house():
#     house = input("House: ")
#     return house
# if __name__ == "__main__":
#     main()

# Example 3
# - implement a simpler function to return both name, house from 1 function
# - only Python allows to return 2 variables inside a function...
# def main():
#     # destructure name, house from get_student function
#     name, house = get_student()
#     print(f"{name} from {house}")
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house
# if __name__ == "__main__":
#     main()

# Example 4
# - use a "TUPLE" (key/value pair) to destructure
# def main():
#     # destructure name, house as student "tuple" from get_student function
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return a TUPLE ()
#     return (name, house)
# if __name__ == "__main__":
#     main()

# Example 5
# - use a LIST
# def main():
#     # destructure name, house as student "list" from get_student function
#     student = get_student()
#     # check: if current student is Padma we should match house to Ravenclaw
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # return a LIST
#     return [name, house]
# if __name__ == "__main__":
#     main()

# Example 6
# - use a DICTIONARY
# def main():
#     # destructure name, house as student "dictionary" from get_student function
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")
# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student
# if __name__ == "__main__":
#     main()

# Example 7
# - use a DICTIONARY -> OK too, but less readability
def main():
    # initialize student "dictionary"
    student = get_student()
    # check: if student's name is "Padma" we'll update it to house of Ravenclaw
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")
def get_student():
    # prompt user for name and house
    name = input("Name: ")
    house = input("House: ")
    # return a dictionary with name, house
    return {
        "name": name,
        "house": house,
    }
if __name__ == "__main__":
    main()
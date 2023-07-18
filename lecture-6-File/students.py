# Read a .csv file

# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         # print(row)
#         print(f"{row[0]} is in {row[1]}")
#         # Hermione is in Gryffindor
#         # Harry is in Gryffindor
#         # Ron is in Gryffindor
#         # Draco is in Slytherin


# Example 2
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
        # Hermione is in Gryffindor
        # Harry is in Gryffindor
        # Ron is in Gryffindor
        # Draco is in Slytherin

# Example 3
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # temporarily append string to []
#         students.append(f"{name} is in {house}")
# # iterate over students []
# for student in sorted(students):
#     print(student)

# Example 4
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # initialize student {} with 2 keys
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         # append dict to students []
#         students.append(student)
# # iterate over students []
# for student in students:
#     print(f"{student['name']} is in {student['house']}")
#     # Hermione is in Gryffindor
#     # Harry is in Gryffindor
#     # Ron is in Gryffindor
#     # Draco is in Slytherin

# Example 5
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # initialize student {} with keys
#         student = {
#             "name": name,
#             "house": house,
#         }
#         # append dict to students []
#         students.append(student)
# # iterate over students []
# for student in students:
#     print(f"{student['name']} is in {student['house']}")

# Example 6
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # initialize student {} with keys
#         student = {
#             "name": name,
#             "house": house,
#         }
#         # append dict to students []
#         students.append(student)
# # temporary function
# def get_name(student):
#     return student["name"]
# # iterate over students; sort in reverse order
# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")

# Example 7 -> Lambda function (anonymous function)
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # initialize student {} with keys
        student = {
            "name": name,
            "house": house,
        }
        # append dict to students []
        students.append(student)
# lambda (anonymous function)
for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")

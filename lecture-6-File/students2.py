# students = []
# with open("students2.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {
#             "name": name,
#             "home": home,
#         }
#         students.append(student)
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
#     # ValueError: too many values to unpack -> students2.csv has too many values

# Example 2
# import csv
# students = []
# with open("students2.csv") as file:
#     # read from csv directly
#     reader = csv.reader(file)
#     # iterate from reader
#     for row in reader:
#         students.append({
#             "name": row[0],
#             "home": row[1],
#         })
# # iterate sorted students []
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
#     # Draco is from Malfoy Manor
#     # Harry is from Number Four
#     # Ron is from The Burrow

# Example 3
# import csv
# students = []
# with open("students2.csv") as file:
#     reader = csv.reader(file)
#     # destructure name, home in reader
#     for name, home in reader:
#         students.append({
#             "name": name,
#             "home": home,
#         })
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
#     # Draco is from Malfoy Manor
#     # Harry is from Number Four, Privet Drive
#     # Ron is from The Burrow

# Example 4 -> use csv.DictReader: csv will read as dictionary of columns
import csv
students = []
with open("students2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # students.append({
        #     "name": row["name"],
        #     "home": row["home"],
        # })
        # OR
        students.append(row) # since DictReader is already "reading" all columns
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
    # Draco is from Malfoy Manor
    # Harry is from Number Four, Privet Drive
    # Ron is from The Burrow
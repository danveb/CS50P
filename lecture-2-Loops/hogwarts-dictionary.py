students = {
    "Hermione": "Griffyndor",
    "Harry": "Griffyndor",
    "Draco": "Slytherin",
}

# Iterate over Dictionary?
for student in students:
    print(student, students[student], sep=", ")
    # Hermione, Griffyndor
    # Harry, Griffyndor
    # Draco, Slytherin

# A Dictionary inside a List?
students = [
    {
        "name": "Hermione",
        "house": "Griffyndor",
        "patronus": "Otter",
    },
    {
        "name": "Harry",
        "house": "Griffyndor",
        "patronus": "Otter",
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None,
    },
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
    # Hermione, Griffyndor
    # Harry, Griffyndor
    # Draco, Slytherin
    # Hermione, Griffyndor, Otter
    # Harry, Griffyndor, Otter
    # Draco, Slytherin, None


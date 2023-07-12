students = ["Harry", "Hermione", "Ron"]
print(students[0]) # "Harry"
print(students[1]) # "Hermione"
print(students[2]) # "Ron"

# iterate through the list?
for student in students:
    print(student) # Harry, Hermione, Ron

# check length of list?
length_students = len(students) # 3
print(length_students)

for i in range(len(students)):
    print(i + 1, students[i])
    # 1 Harry
    # 2 Hermione
    # 3 Ron

for i in range(len(students)):
    print(i)
    # 0
    # 1
    # 2
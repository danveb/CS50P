# Example 1
# # name = input("What's your name? ")
# # print(f"Hello {name}")

# # initialize an empty list []
# names = []
# for _ in range(3):
#     name = input("What's your name? ")
#     names.append(name)

# # print(names) # ["Danny", "Jake", "Geoff"]

# Example 2
# # manually sort names [] in ascending order
# for name in sorted(names):
#     print(f"Hello {name}")
#     # Hello Danny
#     # Hello John
#     # Hello Sil

# Example 3
# name = input("What's your name? ")
# # open file "names.txt" and "write" keyword
# file = open("names.txt", "w")
# # write on the file
# file.write(name)
# # close the file
# file.close()

# Example 4
# name = input("What's your name? ")
# # append "a" in files but in a new line
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# Example 5
# name = input("What's your name? ")
# # use "with" keyword to automatically close the file once done
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# Example 6
# # open "names.txt" as read-only
# with open("names.txt", "r") as file:
#     # read from file
#     lines = file.readlines()
# # iterate over lines
# for line in lines:
#     # strip each line
#     print("Hello", line.rstrip())
#     # Hello Danny
#     # Hello Harry
#     # Hello Sora

# Example 7
# names = []
# with open("names.txt") as file:
#     for line in file:
#         # append each stripped line to []
#         names.append(line.rstrip())
# # iterate sorted []
# for name in sorted(names):
#     print(f"Hello {name}")
#     # Hello Danny
#     # Hello Harry
#     # Hello Sora

# Example 8
# with open("names.txt") as file:
#     for line in sorted(file):
#         print("Hello", line.rstrip())
#         # Hello Danny
#         # Hello Harry
#         # Hello Sora

# Example 9
# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names, reverse=True):
#     print(f"Hello {name}")
#     # Hello Sora
#     # Hello Harry
#     # Hello Danny


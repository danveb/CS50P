name = input("What's your name? ")

# Example #1
# match name:
#     case "Harry":
#         print("Griffyndor")
#     case "Hermione":
#         print("Griffyndor")
#     case "Ron":
#         print("Griffyndor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who again?")

# Example #2
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffyndor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who this?")
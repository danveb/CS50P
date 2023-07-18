# Sorting Hat

# import random

# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     # method
#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))

# # instantiate hat from Hat class
# hat = Hat()
# hat.sort("Harry") # Harry is in Ravenclaw

# Example 2
import random

class Hat:
    # initialize houses as a list []
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # classmethod decorator -> function we can use to add functionality to a class as a whole
    @classmethod
    def sort(cls, name): # cls -> as class
        print(name, "is in", random.choice(cls.houses))

# no need to instantiate a class Object, we'll just sort on Hat class directly
Hat.sort("Harry") # Harry is in Ravenclaw
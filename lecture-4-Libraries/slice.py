house = ["LA", "Irvine", "Chicago"]

# print(house[0]) # slice 0th index # LA
# print(house[1]) # slice 1st index # Irvine
# print(house[1:]) # slice from 1st index to no end # ["Irvine", "Chicago"]
print(house[1:-1]) # slice from 1st index to -1 index, which is counting to left # ["Irvine"]
print(house[0:2]) # slice from 0th index to 2nd index NOT inclusive # ["LA", "Irvine"]

# Example 1
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# iterate over sys.argv and slice from 1st index to no end
for arg in sys.argv[1:]:
    print("Hello my name is", arg)

# $ python slice.py Danny
# Hello my name is Danny

# $ python slice.py Danny Cat Dog
# Hello my name is Danny
# Hello my name is Cat
# Hello my name is Dog
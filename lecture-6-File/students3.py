# csv.writer ->

# import csv

# name = input("What's your name? ")
# home = input("Where's your home? ")

# # open csv file for writing on file
# with open("students3.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

# csv.DictWriter -> allows to write as dictionary
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

# open csv file for writing on file
with open("students3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({
        "name": name,
        "home": home
    })
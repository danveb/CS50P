# Implement a Python program that prompts users to input a fruit (case-insensitive)
# output number of calories in one portion of that fruit
# users will input fruits exactly as written in the poster
# ignore any input that's not a fruit

fruits = [
    {
        "name": "apple",
        "calories": 130,
    },
    {
        "name": "avocado",
        "calories": 50,
    },
    {
        "name": "banana",
        "calories": 110,
    },
    {
        "name": "cantaloupe",
        "calories": 50,
    },
    {
        "name": "grapefruit",
        "calories": 60,
    },
    {
        "name": "grapes",
        "calories": 90,
    },
    {
        "name": "honeydew melon",
        "calories": 50,
    },
    {
        "name": "kiwifruit",
        "calories": 90,
    },
    {
        "name": "lemon",
        "calories": 15,
    },
    {
        "name": "lime",
        "calories": 20,
    },
    {
        "name": "nectarine",
        "calories": 60,
    },
    {
        "name": "orange",
        "calories": 80,
    },
    {
        "name": "peach",
        "calories": 60,
    },
    {
        "name": "pear",
        "calories": 100,
    },
    {
        "name": "pineapple",
        "calories": 50,
    },
    {
        "name": "plums",
        "calories": 70,
    },
    {
        "name": "strawberries",
        "calories": 50,
    },
    {
        "name": "sweet cherries",
        "calories": 100,
    },
    {
        "name": "tangerine",
        "calories": 50,
    },
    {
        "name": "watermelon",
        "calories": 80,
    },
]

# for fruit in fruits:
#     print(fruit["name"])

def main():
    # prompt user for a fruit
    user_input = input("Item: ").lower()
    for fruit in fruits:
        if user_input in fruit["name"]:
            if user_input == fruit["name"]:
                print(f"Calories: {fruit['calories']}")

main()
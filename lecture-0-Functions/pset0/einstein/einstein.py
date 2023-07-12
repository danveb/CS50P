# Implement a Python program that promps user for mass as an integer (in kg)
# output the number of Joules as integer
# assume user will input an integer

# Einstein formula: E = mc^2
# - E: energy
# - m: mass (kg)
# - c: speed of light (m/s)

def main():
    """Calculate Einstein's formula"""
    # m: get user input as integer
    user_input = int(input("m: "))
    # c: initialize speed of light
    speed_of_light = 300000000
    # calculate E=mc^2
    output = user_input * speed_of_light ** 2
    print("E:", output)

main()
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"This is a {self.model} from {self.make}"

    # classmethod of "GET"
    @classmethod
    def get(cls):
        make = input("Make: ")
        model = input("Model: ")
        return cls(make, model)

def main():
    # instantiate vehicle on class Vehicle
    vehicle = Vehicle.get()
    print(vehicle) # This is a CX5 from Mazda

if __name__ == "__main__":
    main()
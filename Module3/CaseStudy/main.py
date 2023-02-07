# Python V3.9.0

class Vehicle():
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

if __name__ == "__main__":
    automobile = Automobile(type = None, year = None, make = None, model = None, doors = None, roof = None)
    automobile.type = input("What type of vehicle do you have? ")
    if automobile.type == "car":
        automobile.year = int(input("What is the car's year? "))
        automobile.make = input("What is the car's make? ")
        automobile.model = input("What is the car's model? ")
        automobile.doors = int(input("How many doors does the car have? (2 or 4) "))
        automobile.roof = input("What kind of roof does the car have? (solid or sun roof) ")

        print("Vehicle type: " + automobile.type)
        print("Year: " + str(automobile.year))
        print("Make: " + automobile.make)
        print("Model: " + automobile.model)
        print("Number of doors: " + str(automobile.doors))
        print("Type of roof: " + automobile.roof)

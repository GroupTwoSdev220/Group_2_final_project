#Minh Tong 
#M03 Lab 
#4/6/2024
#a programm to ask the user to input what type of vehicle they have. 

#first super class

class Vehicle:
    vehicle_type = ""

#second super class

class Automobile(Vehicle):
    year = ""
    make = ""
    model = ""
    doors = ""
    roof = ""

#main part of the code
def main():
    vehicle = Vehicle()
    vehicle.vehicle_type = input("Enter the vehicle type: ")
    car = Automobile()
    car.year = input("Enter the year: ")
    car.make = input("Enter the make: ")
    car.model = input("Enter the model: ")
    car.doors = input("Enter the number of doors (2 or 4): ")
    car.roof = input("Enter the type of roof (solid or sun roof): ")

    print("\nCar Details:")
    print(f"Vehicle type: {vehicle.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")

if __name__ == "__main__":
    main()
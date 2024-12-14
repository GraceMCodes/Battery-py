class Vehicle:
    def move(self):
        pass  # This is a placeholder method to be overridden by subclasses

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Create instances of each vehicle
vehicles = [Car(), Plane(), Boat()]

# Iterate through each vehicle and call move()
for vehicle in vehicles:
    vehicle.move()

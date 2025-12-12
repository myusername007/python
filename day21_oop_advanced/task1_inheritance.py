class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        return "Vehicle is driving"
    
class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def drive(self):
        return f"Car {self.brand} is driving at {self.speed} km/h"
    
car = Car("Skoda Octavia A5", 180, 4)
print(car.drive())
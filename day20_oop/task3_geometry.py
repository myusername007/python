import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle with radius: {self.radius}, Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"
    
circle = Circle(10)
print(circle)

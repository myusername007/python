class Animal:
    def __init__(self):
        pass
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
def animal_sound(animal):
    print(animal.speak())

animals = [Dog(), Cat()]
for a in animals:
    animal_sound(a)